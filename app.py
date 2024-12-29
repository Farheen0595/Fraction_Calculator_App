import streamlit as st
from fractions import Fraction

def main():
    st.title("Fraction Calculator")
    
    st.sidebar.header("Fraction Inputs")
    
    # Input for First Fraction
    numerator1 = st.sidebar.number_input("Numerator of Fraction 1", value=1, step=1)
    denominator1 = st.sidebar.number_input("Denominator of Fraction 1", value=1, step=1)
    fraction1 = Fraction(numerator1, denominator1)

    # Input for Second Fraction
    numerator2 = st.sidebar.number_input("Numerator of Fraction 2", value=1, step=1)
    denominator2 = st.sidebar.number_input("Denominator of Fraction 2", value=1, step=1)
    fraction2 = Fraction(numerator2, denominator2)
    
    st.write("### Fractions Entered:")
    st.write(f"Fraction 1: {fraction1}")
    st.write(f"Fraction 2: {fraction2}")
    
    # Arithmetic Operations
    st.write("### Results of Arithmetic Operations:")
    st.write(f"Addition: {fraction1 + fraction2}")
    st.write(f"Subtraction: {fraction1 - fraction2}")
    st.write(f"Multiplication: {fraction1 * fraction2}")
    try:
        st.write(f"Division: {fraction1 / fraction2}")
    except ZeroDivisionError:
        st.write("Division: Undefined (denominator of second fraction is zero)")
    
    # Conversion to Float
    st.write("### Fraction to Float Conversion:")
    st.write(f"Fraction 1 as Float: {fraction1.numerator / fraction1.denominator}")
    st.write(f"Fraction 2 as Float: {fraction2.numerator / fraction2.denominator}")

if __name__ == "__main__":
    main()
