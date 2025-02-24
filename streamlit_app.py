import streamlit as st
import math

def calculate_subnet_mask(class_type, num_subnets, max_hosts):
    class_masks = {
        'A': '255.0.0.0',
        'B': '255.255.0.0',
        'C': '255.255.255.0'
    }
    
    if class_type not in class_masks:
        return "Ошибка: Неверный класс сети"
    
    base_mask = class_masks[class_type]
    base_bits = {'A': 8, 'B': 16, 'C': 24}[class_type]
    
    needed_subnet_bits = math.ceil(math.log2(num_subnets))
    needed_host_bits = math.ceil(math.log2(max_hosts + 2))  # +2 для сетевого и широковещательного адресов
    
    if needed_subnet_bits + needed_host_bits > (32 - base_bits):
        return "Ошибка: Невозможно создать такое разбиение"
    
    new_mask_bits = base_bits + needed_subnet_bits
    new_mask = ("1" * new_mask_bits + "0" * (32 - new_mask_bits))
    subnet_mask = ".".join(str(int(new_mask[i:i+8], 2)) for i in range(0, 32, 8))
    
    return subnet_mask

st.title("Калькулятор маски подсети")

class_type = st.selectbox("Выберите класс сети", ['A', 'B', 'C'])
num_subnets = st.number_input("Количество подсетей", min_value=1, step=1)
max_hosts = st.number_input("Максимальное количество хостов в подсети", min_value=1, step=1)

if st.button("Рассчитать маску подсети"):
    result = calculate_subnet_mask(class_type, num_subnets, max_hosts)
    st.write(f"Маска подсети: {result}")