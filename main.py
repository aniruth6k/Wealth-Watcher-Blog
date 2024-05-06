import streamlit as st
import pandas as pd

# Create a mock data frame for updates
updates = pd.DataFrame({
    'version': ['1.0.0', '1.0.1', '1.1.0'],
    'date': ['2023-05-06', '2023-05-13', '2023-05-20'],
    'description': [
        'Initial release',
        'Bug fixes and performance improvements',
        'Added new commands and final release'
    ],
    'upvotes': [10, 5, 2],
    'downvotes': [2, 1, 0],
    'reviews': [
        ['Great bot!', 'Could use some more features.'],
        ['Faster than before!', 'User interface needs to be imporved.'],
        ['Usability has improved significantly', 'Minor bugs were removed.']
    ]
})

# Function to display updates
def display_updates():
    for i, update in updates.iterrows():
        st.header(f"Version {update['version']} - {update['date']}")
        st.write(update['description'])
        
        upvote, downvote = st.columns(2)
        with upvote:
            upvote_count = st.button(f"👍 {update['upvotes']}", key=f"upvote_{i}")
            if upvote_count:
                updates.at[i, 'upvotes'] += 1
        with downvote:
            downvote_count = st.button(f"👎 {update['downvotes']}", key=f"downvote_{i}")
            if downvote_count:
                updates.at[i, 'downvotes'] += 1
        
        if update['reviews']:
            st.subheader('Reviews')
            for review in update['reviews']:
                st.write(review)
        
        st.write('---')

# Streamlit app
def app():
    st.title('Wealth Watcher Blog')
    display_updates()

if __name__ == '__main__':
    app()
