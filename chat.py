def chat(userInput):
    # Get weather data for Riyadh
    weather_data = getweather('riyadh')
    
    # Generate response from the model
    res = MODEL.invoke({"weather": weather_data, "input": userInput, "history": st.session_state.messages})
    
    # Append user and assistant messages to session state
    st.session_state.messages.append(("user", userInput))  # Storing as a tuple (role, message)
    st.session_state.messages.append(("assistant", res['text']))  # Storing as a tuple (role, message)
    
    # Retain only the last N messages for context
    MAX_HISTORY = 10
    if len(st.session_state.messages) > MAX_HISTORY:
        st.session_state.messages = st.session_state.messages[-MAX_HISTORY:]
    
    return res['text']
