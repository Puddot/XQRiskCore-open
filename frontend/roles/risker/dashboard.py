# frontend/roles/risker/dashboard.py

from core.request_context import RequestContext
from frontend.shared.dashboard_template import render_role_dashboard
import streamlit as st

def render(ctx: RequestContext):
    try:
        render_role_dashboard(ctx, role_label="Risk Manager Console", sidebar_key="risker_sidebar")
    except Exception as e:
        st.error("❌ Risk Manager dashboard failed to load.")
        st.exception(e) 
