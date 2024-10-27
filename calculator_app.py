import streamlit as st 
st.title("calculator")
st.write('1.Addition')
st.write('2.Subtraction')
st.write('3.Multiplication')
st.write('4.Division')
choice=st.number_input("Enter your choice ")
num1=st.number_input('Enter first number')
num2=st.number_input('Enter second number')
if st.button('click me'):
    if choice==1:
        st.write(num1+num2)
    elif choice==2:
        st.write(num1-num2)
    elif choice==3:
        st.write(num1*num2)   
    elif choice==4:
        st.write(num1/num2)
    else:
        st.write('Please enter a valid choice')            

