import streamlit as st

if st.button("streamlit_option_menu"):
    from streamlit_option_menu import option_menu

    with st.sidebar:
        selected = option_menu(
            "Main Menu",
            ["Home", "Settings"],
            icons=["house", "gear"],
            menu_icon="cast",
            default_index=1,
        )
        selected


if st.button("streamlit_cookie_manager"):
    import streamlit as st
    from cookie_manager import CookieManager

    cookies = CookieManager()

    st.write("Current cookies:", cookies.get_all())

    if st.button("Set Cookie"):
        cookies.set("my_cookie", "cookie_value", expires_at="2024-12-31T23:59:59")
        st.write("Cookie set!")

if st.button("antd"):
    import streamlit as st
    import streamlit_antd_components as sac

    btn = sac.buttons(
        items=["button1", "button2", "button3"],
        index=0,
        format_func="title",
        align="center",
        direction="horizontal",
        radius="lg",
        return_index=False,
    )
    st.write(f"The selected button label is: {btn}")

if st.button("st aggrid"):
    from st_aggrid import AgGrid
    import pandas as pd

    df = pd.read_csv(
        "https://raw.githubusercontent.com/fivethirtyeight/data/master/airline-safety/airline-safety.csv"
    )
    AgGrid(df)

if st.button("streamlit_autorefresh"):
    import streamlit as st
    from streamlit_autorefresh import st_autorefresh

    # Run the autorefresh about every 2000 milliseconds (2 seconds) and stop
    # after it's been refreshed 100 times.
    count = st_autorefresh(interval=2000, limit=100, key="fizzbuzzcounter")

    # The function returns a counter for number of refreshes. This allows the
    # ability to make special requests at different intervals based on the count
    if count == 0:
        st.write("Count is zero")
    elif count % 3 == 0 and count % 5 == 0:
        st.write("FizzBuzz")
    elif count % 3 == 0:
        st.write("Fizz")
    elif count % 5 == 0:
        st.write("Buzz")
    else:
        st.write(f"Count: {count}")

if st.button("st feedback"):
    from streamlit_feedback import streamlit_feedback

    feedback = streamlit_feedback(feedback_type="thumbs")
    feedback

if st.button("streamlit_folium"):
    import streamlit as st
    import folium
    from streamlit_folium import st_folium

    map_center = [45.5236, -122.6750]
    m = folium.Map(location=map_center, zoom_start=13)

    st_folium(m, width=700, height=500)
