from services.base import BaseService
from services.schema import PropertyPreferencesInsert, PropertyPreferencesUpdate
from uuid import UUID
from typing import Optional, Dict, List
import logging

logger = logging.getLogger(__name__)

class PropertyService(BaseService):
            
    def bulk_insert_properties(self, properties: List[Dict]) -> Dict:

        """Bulk insert scraped properties into database"""
        inserted = 0
        errors = []
        
        for prop in properties:
            try:
                # Remove fields that shouldn't be in database or are auto-generated
                prop_data = {
                    'address': prop.get('address'),
                    'rent': prop.get('price'),
                    'rent_psf': prop.get('price_psf'),
                    'num_bedrooms': prop.get('bedrooms'),
                    'num_bathrooms': prop.get('bathrooms'),
                    'sqft': prop.get('area_sqft'),
                    'property_type': prop.get('unit_type'),
                    'listing_status': prop.get('availability'),
                    'mrt_info': prop.get('mrt_info'),
                    'listing_id': prop.get('listing_id'),
                    # Add any other fields that match your database schema
                }
                
                # Remove None values
                prop_data = {k: v for k, v in prop_data.items() if v is not None}
                
                # Insert into database
                self.client.table("properties").insert(prop_data).execute()
                inserted += 1
                
            except Exception as e:
                from core.exceptions import OperationError
                error_msg = f"Failed to insert property {prop.get('listing_id', 'unknown')}: {str(e)}"
                errors.append(error_msg)
                logger.warning(error_msg)
                continue
        
        return {
            'success': True,
            'inserted': inserted,
            'total': len(properties),
            'errors': errors
        }
    
    def check_duplicate_listing(self, listing_id: str) -> bool:
        """Check if a listing already exists in database"""
        try:
            response = self.client.table("properties").select("property_id").eq("listing_id", listing_id).execute()
            return len(response.data) > 0
        except Exception as e:
            logger.error(f"Duplicate check failed: {str(e)}")
            return False
