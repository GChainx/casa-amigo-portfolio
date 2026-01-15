import os
import time
import streamlit as st
from typing import List, Dict, Any

from config import ConfigManager
from core import ChatbotEngine, DocumentIndexManager


class StreamlitApp:
    """Manages the Streamlit UI and user interactions."""

    idle_icon = os.path.join(os.path.dirname(__file__), "..", "assets", "blink_robot_avatar.gif")
    thinking_icon = os.path.join(os.path.dirname(__file__), "..", "assets", "load_robot_avatar.gif")
    user_icon = os.path.join(os.path.dirname(__file__), "..", "assets", "user_avatar.png")

    def _render_sidebar(self):
        with st.sidebar:
            logo_path = os.path.join(os.path.dirname(__file__), "..", "assets", "logo.png")
            
    def _display_chat_history(self):
        for msg in st.session_state["messages"]:
            role = msg["role"]
            content = msg["content"]
            avatar =self.user_icon if role == "user" else self.idle_icon
            bubble_class = "ca-user" if role == "user" else "ca-assist"

            with st.chat_message(role, avatar=avatar):
                st.markdown(f'<div class="ca-bubble {bubble_class}">{content}</div>', unsafe_allow_html=True)

    def _handle_user_input(self):
        if user_query := st.chat_input("Type your message..."):
            st.session_state["messages"].append({"role": "user", "content": user_query})
            with st.chat_message("user", avatar=self.user_icon):
                st.markdown(f'<div class="ca-bubble ca-user">{user_query}</div>', unsafe_allow_html=True)
            
            with st.chat_message("assistant", avatar=self.thinking_icon):
                placeholder = st.empty()
                for _ in range(3):
                    dots_html = "<span class='ca-dot'></span>" * 3
                    placeholder.markdown(f"<div class='ca-typing'>{dots_html}</div>", unsafe_allow_html=True)
                    time.sleep(0.35)
                response = self.chatbot.get_response(user_query)
                placeholder.markdown(f"<div class='ca-bubble ca-assist'>{response}</div>", unsafe_allow_html=True)

            st.session_state["messages"].append({"role": "assistant", "content": response})
            st.rerun()