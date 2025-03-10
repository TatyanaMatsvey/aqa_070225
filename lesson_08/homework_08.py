"""
Реалізувати функцію `sum_numbers_in_list(input_list)`, яка приймає список рядків,
де кожен рядок містить числа, розділені комами. Функція повинна повертати список
із сум чисел для кожного рядка або відповідне повідомлення про помилку у
випадку некоректних даних.


#### **Приклади виклику функції:**
```python
sum_numbers_in_list(["1,2,3", "4,0,6"])  # [6, 10]
sum_numbers_in_list(["1,2,3", "asas7,8,9", "4,0,6"])  # [6, "Не можу це зробити!", 10]
sum_numbers_in_list(["1,2,3,4", 7])  # [10, "Не можу це зробити! AttributeError"]
sum_numbers_in_list([])  # ValueError
sum_numbers_in_list("21")  # ValueError
```
"""




def sum_numbers_in_list(string_list: list):
   """Повертає список сум чисел зі списку строк,
   які складаються з чисел, розділених комою."""


   if not isinstance(string_list, list):
       raise ValueError("ValueError")


   if not string_list:
       raise ValueError("ValueError")


   result = []
   for item in string_list:
       try:
           if not isinstance(item, str):
               raise AttributeError("AttributeError")


           numbers = map(int, item.split(","))
           result.append(sum(numbers))
       except ValueError:
           result.append("Не можу це зробити!")
       except AttributeError as e:
           result.append(f"Не можу це зробити! {e}")


   return result




if __name__ == "__main__":
   output = sum_numbers_in_list(["1,2,3", "4,0,6"])
   print(output)


   output = sum_numbers_in_list(["1,2,3", "4/0,6", "asas7,8,9"])


   print(sum_numbers_in_list(["1,2,3", "4,0,6"]))  # [6, 10]
   print(sum_numbers_in_list(["1,2,3", "asas7,8,9", "4,0,6"]))  # [6, "Не можу це зробити!", 10]
   print(sum_numbers_in_list(["1,2,3,4", 7]))  # [10, "Не можу це зробити! AttributeError"]
   print(sum_numbers_in_list([]))  # ValueError
   print(sum_numbers_in_list("21"))  # ValueError

