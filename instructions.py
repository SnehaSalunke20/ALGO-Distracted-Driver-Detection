import streamlit as st


def instructions_page(_gettext=None):
    # --- Centered title ---
    st.markdown(
        "<h2 style='text-align: center;'> Instructions for Recording Respiratory Sounds</h2>",
        unsafe_allow_html=True
    )

    # --- Navigation button ---
    if st.button("➡️ Next", key="next_top"):
        st.session_state["show_dashboard"] = True
        st.rerun()

    # Custom CSS
    st.markdown(
        """
        <style>
        .blue-box {
            background-color: #799BE6;
            color: white;
            padding: 15px;
            border-radius: 12px;
            margin-bottom: 15px;
            margin-left: 28px;
            box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.1);
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Two groups side by side
    col1, col2 = st.columns(2, gap="medium")

    # --- LEFT COLUMN ---
    with col1:
        # 1. Choose Your Device (local image)
        with st.container():
            cols = st.columns([3, 1])
            with cols[0]:
                st.markdown(
                    """
                    <div class="blue-box">
                        <h3>1. Choose Your Device</h3>
                        <ul>
                            <li><b>Electronic stethoscope</b> → place on chest as instructed.</li>
                            <li><b>Microphone / Smartphone mic</b> → hold close to chest or throat.</li>
                        </ul>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
            with cols[1]:
                st.image("ui_assets/images/instruction1.png", width=100)  

        # 2. Find a Quiet Place
        with st.container():
            cols = st.columns([3, 1])
            with cols[0]:
                st.markdown(
                    """
                    <div class="blue-box">
                        <h3>2. Find a Quiet Place</h3>
                        <ul>
                            <li>Go to a quiet room without background noise (TV, fan, people talking).</li>
                            <li>Sit upright and relax.</li>
                        </ul>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
            with cols[1]:
                st.image("ui_assets/images/instruction2.png", width=100)

        # 3. Place the Device Correctly
        with st.container():
            cols = st.columns([3, 1])
            with cols[0]:
                st.markdown(
                    """
                    <div class="blue-box">
                        <h3>3. Place the Device Correctly</h3>
                        <ul>
                            <li>If <b>stethoscope</b> → place the chest piece on upper chest, back, or sides.</li>
                            <li>If <b>microphone</b> → hold it 2–5 cm from chest or throat.</li> 
                        </ul>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
            with cols[1]:
                st.image("ui_assets/images/instruction3.png", width=100)

    # --- RIGHT COLUMN ---
    with col2:
        # 4. Start Recording
        with st.container():
            cols = st.columns([3, 1])
            with cols[0]:
                st.markdown(
                    """
                    <div class="blue-box">
                        <h3>4. Start Recording</h3>
                        <ul>
                            <li>Use your app/recorder to start recording in <b>WAV format</b>.</li>
                            <li>Breathe normally for about <b>20 seconds</b>.</li>
                        </ul>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
            with cols[1]:
                st.image("ui_assets/images/instruction4.png", width=100)

        # 5. During Recording
        with st.container():
            cols = st.columns([3, 1])
            with cols[0]:
                st.markdown(
                    """
                    <div class="blue-box">
                        <h3>5. During Recording</h3>
                        <ul>
                            <li>Do not talk, cough, or laugh.</li>
                            <li>Stay still and breathe naturally.</li>
                        </ul>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
            with cols[1]:
                st.image("ui_assets/images/instruction6.png", width=100)

        # 6. Save the File
        with st.container():
            cols = st.columns([3, 1])
            with cols[0]:
                st.markdown(
                    """
                    <div class="blue-box">
                        <h3>6. Save the File</h3>
                        <ul>
                            <li>Stop the recording after ~<b>40 seconds</b>.</li>
                            <li>Save it with a <b>clear name</b>.</li>
                        </ul>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
            with cols[1]:
                st.image("ui_assets/images/instruction5.png", width=100)

    st.info("ℹ️ Tip: Proper placement and quiet surroundings improve analysis accuracy.")
