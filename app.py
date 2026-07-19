import streamlit as st

def render_comprehensive_dispatcher_pitch():
    st.set_page_config(page_title="Professional Dispatcher Pitch", layout="wide")
    
    st.title("🚛 Strategic Carrier Partnership Pitch")
    st.subheader("Objective: Transition from 'Caller' to 'Strategic Partner'")
    st.markdown("---")

    # MODULE 1: THE DISCOVERY & AUTHORITY OPENER
    st.header("Module 1: Establishing Professional Authority")
    st.markdown("""
    * **Opening:** 'Hi [Owner Name], my name is Ahsan. I’ve been analyzing lane trends in your primary operating regions, and I noticed your fleet is consistently active in [Specific Region/Lane]. I’m calling to discuss a partnership aimed at optimizing your current lane density.'
    * **The Hook:** 'I don't just move trucks; I manage them as profit centers. I am currently looking for one or two high-performance carriers to integrate into my dispatching infrastructure for Q3/Q4 capacity planning.'
    * **The Qualification:** 'Before we go further, I want to ensure my current market data aligns with your equipment type. Are you currently running [e.g., Dry Van/Reefer] or are you planning to shift your focus to different freight lanes in the coming months?'
    """)

    st.divider()

    # MODULE 2: THE VALUE PROPOSITION (DEEP DIVE)
    st.header("Module 2: The Value Proposition (Operational ROI)")
    st.markdown("""
    * **Data-Driven Routing:** 'I utilize historical market rate indices to forecast high-paying loads before they hit the general load boards. My objective is to bridge the gap between spot market volatility and your fixed operational costs.'
    * **Margin Maximization:** 'Most dispatchers focus on simple load-to-truck matching. I focus on **Rate-per-Mile (RPM) Optimization**. I cross-reference fuel surcharges, detention time risks, and upcoming market shifts to ensure your gross revenue is consistently above the market average.'
    * **Administrative Freedom:** 'I manage the entire back-end lifecycle: carrier onboarding packets, rate confirmation negotiations, detention/layover invoicing, and OS&D reporting. This allows your drivers to maintain maximum HOS (Hours of Service) efficiency without being interrupted by brokers.'
    * **Communication Protocol:** 'I operate on a transparent feedback loop. You will receive a daily summary of your lane profitability, fuel costs, and broker relationships so that you stay in full control of your business assets.'
    """)

    st.divider()

    # MODULE 3: THE STRATEGIC CLOSING & PARTNERSHIP PATH
    st.header("Module 3: Strategic Closing & Qualification")
    st.markdown("""
    * **Addressing the Need:** 'I understand you might already have dispatching in place. However, the market is currently shifting. I am proposing a **two-week pilot engagement** where I handle your most challenging lanes to demonstrate a measurable increase in your average daily net revenue.'
    * **Call to Action:** 'I don't expect you to take my word for it. Let’s look at your last week's settlement data. If I can show you how to increase your average RPM by [X]% through more effective lane planning, would you be open to an initial test run?'
    * **Next Step:** 'Can we schedule a 10-minute deep dive on [Day of Week] to review your current pain points and see if our operational styles are a match?'
    """)

    st.markdown("---")
    st.info("Strategy Note: When they object, do not defend. Reframe. If they say 'I don't need a dispatcher', respond: 'I completely understand. I'm not looking to replace your current system, but to provide a performance audit of your current lanes to see if there is untapped revenue you’re missing.'")

if __name__ == "__main__":
    render_comprehensive_pitch()
