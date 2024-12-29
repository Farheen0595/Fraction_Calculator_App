import streamlit as st
from fractions import Fraction

def main():
    import streamlit as st
    from fraction import Fraction
    
    st.title("Fraction Calculator")
    
    st.sidebar.header("Input Fractions")
    num1 = st.sidebar.number_input("Numerator 1", value=1, step=1)
    den1 = st.sidebar.number_input("Denominator 1", value=1, step=1)
    num2 = st.sidebar.number_input("Numerator 2", value=1, step=1)
    den2 = st.sidebar.number_input("Denominator 2", value=1, step=1)
    
    try:
        fraction1 = Fraction(num1, den1)
        fraction2 = Fraction(num2, den2)
    
        st.write(f"Fraction 1: {fraction1}")
        st.write(f"Fraction 2: {fraction2}")
    
        operation = st.radio("Choose Operation", ("Add", "Subtract", "Multiply", "Divide"))
    
        if operation == "Add":
            result = fraction1 + fraction2
    
        elif operation == "Subtract":
            result = fraction1 - fraction2
    
        elif operation == "Multiply":
            result = fraction1 * fraction2
            
        elif operation == "Divide":
            result = fraction1 / fraction2
    
        st.success(f"Result: {result}")
    
    except Exception as e:
        st.error(f"Error: {e}")

if __name__ == "__main__":
    main()
