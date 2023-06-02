import tkinter as tk
root = tk.Tk()

schema_list = [[
    [{}], [{}]
]]

action_input_counter = 0
def add_action_input():
    global schema_list
    global action_input_counter  # Declare counter as a global variable
    sub_schema_input = {}
    sub_schema_input_list = []
    new_button = tk.Button(root, text='new action')
    sub_schema_input['button'] = new_button
    sub_schema_input['button'].pack()
    sub_schema_input_list.append(sub_schema_input)
    print(sub_schema_input_list)
    action_input_counter += 1




add_action_input_button = tk.Button(root, text="Add action input", command=add_action_input)
add_action_input_button.pack()


root.title('Rekii tool')
root.geometry("1400x800+10+10")
root.mainloop()
