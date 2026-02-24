import streamlit as st
import json
from datetime import datetime

st.set_page_config(page_title="ABB Sales Presentation Builder", layout="wide", page_icon="🎯")

# Custom CSS for ABB branding
st.markdown("""
    <style>
    .main {
        background-color: #ffffff;
    }
    h1 {
        color: #FF000F;
        font-family: 'ABB', Arial, sans-serif;
    }
    h2, h3 {
        color: #6764f6;
    }
    .stButton>button {
        background-color: #FF000F;
        color: white;
        font-weight: bold;
        border-radius: 5px;
        padding: 10px 24px;
        border: none;
    }
    .stButton>button:hover {
        background-color: #cc0000;
    }
    .success-box {
        padding: 20px;
        border-radius: 10px;
        background-color: #e4e7ff;
        border-left: 5px solid #6764f6;
    }
    </style>
    """, unsafe_allow_html=True)

# Header with ABB branding
st.title("🎯 ABB Sales Presentation Builder")
st.markdown("### Create compelling, customer-centric presentations that win business")
st.markdown("---")

# Initialize session state
if 'form_submitted' not in st.session_state:
    st.session_state.form_submitted = False
if 'form_data' not in st.session_state:
    st.session_state.form_data = None
if 'json_str' not in st.session_state:
    st.session_state.json_str = None
if 'json_filename' not in st.session_state:
    st.session_state.json_filename = None

# Progress indicator
if not st.session_state.form_submitted:
    st.info("📝 **Fill in the form below.** Required fields are marked with *. The more details you provide, the better your presentation will be!")

# Create the form
with st.form("presentation_form"):
    
    # Section 1: Customer & Project Information
    st.header("1️⃣ Customer & Project Information")
    col1, col2 = st.columns(2)
    
    with col1:
        customer_name = st.text_input("Customer Name *", 
                                      placeholder="e.g., Acme Manufacturing",
                                      help="Name of the company/organization")
        channel = st.selectbox("Customer Channel", 
                               ["", "Distributor", "Installer", "Panel Builder", "OEM", "EPC", "End User"],
                               help="Select the customer's business type")
        country = st.text_input("Project Country", 
                               placeholder="e.g., Spain, Germany, USA",
                               help="Where is the project located?")
    
    with col2:
        project_title = st.text_input("Project Title", 
                                     placeholder="e.g., Factory Automation Upgrade",
                                     help="Brief title or name of the project")
        language = st.selectbox("Presentation Language *", 
                               ["English", "Spanish", "German", "French", "Italian", "Portuguese", "Chinese", "Other"],
                               help="Language for the presentation")
        end_user = st.text_input("End User", 
                                placeholder="e.g., Final customer name",
                                help="Who is the final end user? (if different from customer)")
    
    other_players = st.text_area("Other Players/Stakeholders", 
                                 placeholder="List any consultants, contractors, or other parties involved...",
                                 help="List any other relevant parties involved in the project",
                                 height=100)
    
    st.markdown("---")
    
    # Section 2: Industry & Application
    st.header("2️⃣ Industry & Application")
    col3, col4 = st.columns(2)
    
    with col3:
        industry = st.selectbox("Industry Segment *",
                               ["", 
                                "Process Industries (Oil & Gas, Chemicals, Pharmaceuticals)",
                                "Discrete Automation (Automotive, Electronics)",
                                "Energy (Utilities, Renewables)",
                                "Buildings & Infrastructure",
                                "Transportation",
                                "Other"],
                               help="Select the primary industry")
    
    with col4:
        application = st.text_input("Specific Application", 
                                   placeholder="e.g., Motor control, Energy management, HVAC",
                                   help="e.g., Motor control, Energy management, Building automation, etc.")
    
    st.markdown("---")
    
    # Section 3: Buyer Persona
    st.header("3️⃣ Buyer Persona")
    buyer_persona = st.multiselect("Primary Decision-Maker Profile(s)",
                                   ["Technical Buyer (Engineers, Technical Managers)",
                                    "Economic Buyer (C-suite, Procurement)",
                                    "End-User (Operators, Maintenance Teams)",
                                    "Influencer (Consultants, Advisors)"],
                                   help="Select all that apply - who will be in the meeting?")
    
    st.markdown("---")
    
    # Section 4: Meeting Context
    st.header("4️⃣ Meeting Context")
    context = st.selectbox("Meeting Purpose *",
                          ["", 
                           "First time meeting the customer",
                           "Meeting to clarify the scope",
                           "Meeting to explain the quotation",
                           "Meeting to negotiate/close the deal"],
                          help="What is the purpose of this presentation?")
    
    st.markdown("---")
    
    # Section 5: Supporting Materials & Additional Information
    st.header("5️⃣ Supporting Materials & Additional Information")
    st.markdown("*These fields are optional but will significantly improve your presentation quality*")
    
    visit_reports = st.text_area("Visit Reports / Previous Meeting Notes",
                                 placeholder="Summarize key points from previous interactions...",
                                 help="Summary of previous customer interactions",
                                 height=100)
    
    technical_offer = st.text_area("Technical Offer / Specifications",
                                   placeholder="List key technical requirements, voltage levels, capacities, etc...",
                                   help="Key technical requirements or specifications",
                                   height=100)
    
    customer_pain_points = st.text_area("Customer Pain Points / Requirements",
                                        placeholder="e.g., High energy costs, frequent downtime, aging equipment...",
                                        help="What challenges is the customer facing?",
                                        height=100)
    
    competitive_info = st.text_area("Competitive Landscape",
                                    placeholder="e.g., Currently using competitor X, considering alternatives...",
                                    help="Information about competitors or alternative solutions being considered",
                                    height=100)
    
    customer_objectives = st.text_area("Customer Objectives / KPIs",
                                       placeholder="e.g., Reduce energy costs by 20%, improve uptime to 99%...",
                                       help="What are the customer's goals and success metrics?",
                                       height=100)
    
    additional_notes = st.text_area("Additional Notes",
                                    placeholder="Any other relevant information...",
                                    help="Any other relevant information",
                                    height=100)
    
    st.markdown("---")
    
    # Submit button (INSIDE THE FORM)
    col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
    with col_btn2:
        submitted = st.form_submit_button("✅ Generate Presentation Input File", 
                                         use_container_width=True,
                                         type="primary")
    
    # Process form submission
    if submitted:
        # Validate required fields
        if not customer_name or not language or not industry or not context:
            st.error("⚠️ **Please fill in all required fields marked with ***")
            missing_fields = []
            if not customer_name:
                missing_fields.append("Customer Name")
            if not language:
                missing_fields.append("Language")
            if not industry:
                missing_fields.append("Industry")
            if not context:
                missing_fields.append("Meeting Context")
            st.warning("Missing: " + ", ".join(missing_fields))
        else:
            # Collect all form data
            form_data = {
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "customer_info": {
                    "customer_name": customer_name,
                    "channel": channel if channel else "Not specified",
                    "country": country if country else "Not specified",
                    "project_title": project_title if project_title else "Not specified",
                    "language": language,
                    "end_user": end_user if end_user else "Not specified",
                    "other_players": other_players if other_players else "Not specified"
                },
                "industry_application": {
                    "industry_segment": industry,
                    "specific_application": application if application else "Not specified"
                },
                "buyer_persona": buyer_persona if buyer_persona else ["Not specified"],
                "meeting_context": context,
                "supporting_materials": {
                    "visit_reports": visit_reports if visit_reports else "Not provided",
                    "technical_offer": technical_offer if technical_offer else "Not provided",
                    "customer_pain_points": customer_pain_points if customer_pain_points else "Not provided",
                    "competitive_info": competitive_info if competitive_info else "Not provided",
                    "customer_objectives": customer_objectives if customer_objectives else "Not provided",
                    "additional_notes": additional_notes if additional_notes else "Not provided"
                }
            }
            
            # Save to session state
            json_filename = f"presentation_input_{customer_name.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            json_str = json.dumps(form_data, indent=4)
            
            st.session_state.form_submitted = True
            st.session_state.form_data = form_data
            st.session_state.json_str = json_str
            st.session_state.json_filename = json_filename

# OUTSIDE THE FORM - Display results and download button
if st.session_state.form_submitted:
    st.success("✅ **Input file created successfully!**")
    st.balloons()
    
    # Display summary
    st.markdown("### 📋 Summary of Your Input:")
    
    col_sum1, col_sum2 = st.columns(2)
    
    with col_sum1:
        st.markdown("**Customer Information:**")
        st.write(f"• Customer: {st.session_state.form_data['customer_info']['customer_name']}")
        st.write(f"• Channel: {st.session_state.form_data['customer_info']['channel']}")
        st.write(f"• Country: {st.session_state.form_data['customer_info']['country']}")
        st.write(f"• Project: {st.session_state.form_data['customer_info']['project_title']}")
        st.write(f"• Language: {st.session_state.form_data['customer_info']['language']}")
    
    with col_sum2:
        st.markdown("**Meeting Details:**")
        st.write(f"• Industry: {st.session_state.form_data['industry_application']['industry_segment']}")
        st.write(f"• Application: {st.session_state.form_data['industry_application']['specific_application']}")
        st.write(f"• Context: {st.session_state.form_data['meeting_context']}")
        personas = st.session_state.form_data['buyer_persona']
        st.write(f"• Buyer Personas: {', '.join(personas) if personas and personas != ['Not specified'] else 'Not specified'}")
    
    st.markdown("---")
    
    # Download button (NOW OUTSIDE THE FORM - THIS FIXES THE ERROR!)
    st.download_button(
        label="📥 Download Input File (JSON)",
        data=st.session_state.json_str,
        file_name=st.session_state.json_filename,
        mime="application/json",
        use_container_width=True
    )
    
    st.markdown("---")
    st.info("""
    👉 **Next Steps:**
    1. Download the JSON file above
    2. Share it with your ABB AI assistant
    3. The AI will create your customized presentation
    4. Review and refine as needed
    """)
    
    # Option to view full JSON
    with st.expander("🔍 View Full JSON Data"):
        st.json(st.session_state.form_data)
    
    # Reset button
    if st.button("🔄 Create Another Presentation", use_container_width=True):
        st.session_state.form_submitted = False
        st.session_state.form_data = None
        st.session_state.json_str = None
        st.session_state.json_filename = None
        st.rerun()

# Instructions sidebar
st.sidebar.header("ℹ️ How to Use")
st.sidebar.markdown("""
**Quick Start Guide:**

1. **Fill Required Fields** (marked with *)
   - Customer Name
   - Language
   - Industry
   - Meeting Context

2. **Add Details** (optional but recommended)
   - More details = Better presentation
   - Skip what you don't know

3. **Generate & Download**
   - Click the button
   - Download JSON file
   - Share with AI assistant

**Tips for Best Results:**
- Be specific about pain points
- Include customer objectives
- Mention competitive situation
- Add technical requirements
""")

st.sidebar.markdown("---")
st.sidebar.markdown("### 📞 Contact")
st.sidebar.markdown("**Eva de Quintana**")
st.sidebar.markdown("eva.de-quintana@es.abb.com")
st.sidebar.markdown("ABB Spain")

st.sidebar.markdown("---")
st.sidebar.markdown("### 🔗 Resources")
st.sidebar.markdown("[ABB.com](https://www.abb.com)")
st.sidebar.markdown("[ABB Library](https://library.abb.com)")
st.sidebar.markdown("[ABB Ability](https://www.abb.com/abbability)")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 20px;'>
    <p>ABB Sales Presentation Builder | Powered by ABB AI Assistant</p>
    <p style='font-size: 12px;'>© 2026 ABB. All rights reserved.</p>
</div>
""", unsafe_allow_html=True)
