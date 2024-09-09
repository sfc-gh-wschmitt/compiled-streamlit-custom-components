# compiled-streamlit-custom-components

This project facilitates analysis of streamlit bidirectional custom components. 

There are two major components:
* `fetch.py` - a script to fetch wheels and unzip them into downloaded_package.
* `downloaded_package` - a directory containing wheels and assets. 

## Usage
```sh
# package name in kebab-case:
./fetch.py streamlit-option-menu
```

## Packages

#### streamlit-option-menu
* streamlit_option_menu-0.3.13-py3-none-any.whl
* https://github.com/victoryhb/streamlit-option-menu/tree/master 
```python
import streamlit as st
from streamlit_option_menu import option_menu

with st.sidebar:
    selected = option_menu("Main Menu", ["Home", 'Settings'], 
        icons=['house', 'gear'], menu_icon="cast", default_index=1)
    selected
```



#### cookie-manager 
* https://github.com/ktosiek/streamlit-cookies-manager
* cookie_manager-1.2.3-py3-none-any.whl
```python
import streamlit as st
from cookie_manager import CookieManager

cookies = CookieManager()

st.write("Current cookies:", cookies.get_all())

if st.button("Set Cookie"):
    cookies.set("my_cookie", "cookie_value", expires_at="2024-12-31T23:59:59")
    st.write("Cookie set!")
```

####  streamlit-antd-components
* streamlit_antd_components-0.3.2-py3-none-any.whl
* https://github.com/nicedouble/StreamlitAntdComponents
```python
import streamlit as st
import streamlit_antd_components as sac

btn = sac.buttons(
    items=['button1', 'button2', 'button3'],
    index=0,
    format_func='title',
    align='center',
    direction='horizontal',
    radius='lg',
    return_index=False,
)
st.write(f'The selected button label is: {btn}')
```

#### streamlit_aggrid
* streamlit_aggrid-1.0.5-py3-none-any.whl
* https://github.com/PablocFonseca/streamlit-aggrid
```python
from st_aggrid import AgGrid
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/fivethirtyeight/data/master/airline-safety/airline-safety.csv')
AgGrid(df)
```

#### streamlit_autorefresh
* https://github.com/kmcgrady/streamlit-autorefresh
* streamlit_autorefresh-1.0.1-py3-none-any.whl

```python
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
```

#### streamlit_feedback
* streamlit_feedback-0.1.3-py3-none-any.whl
* https://github.com/trubrics/streamlit-feedback/tree/main
```python
from streamlit_feedback import streamlit_feedback
feedback = streamlit_feedback(feedback_type="thumbs")
feedback
```

#### streamlit_folium
* https://github.com/randyzwitch/streamlit-folium
* streamlit_folium-0.22.0-py3-none-any.whl
```python
import streamlit as st
import folium
from streamlit_folium import st_folium

map_center = [45.5236, -122.6750]
m = folium.Map(location=map_center, zoom_start=13)

st_folium(m, width=700, height=500)
```
