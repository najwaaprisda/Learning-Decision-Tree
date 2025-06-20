import tkinter as tk
from sklearn import tree
import matplotlib.pyplot as plt

# Mapping nilai kategorik ke angka
mapping = {
    'Alternate': {'No': 0, 'Yes': 1},
    'Bar': {'No': 0, 'Yes': 1},
    'Fri/Sat': {'No': 0, 'Yes': 1},
    'Hungry': {'No': 0, 'Yes': 1},
    'Patrons': {'None': 0, 'Some': 1, 'Full': 2},
    'Price': {'$': 0, '$$': 1, '$$$': 2},
    'Raining': {'No': 0, 'Yes': 1},
    'Reservation': {'No': 0, 'Yes': 1},
    'Type': {'French': 0, 'Italian': 1, 'Thai': 2, 'Burger': 3},
    'WaitEstimate': {'0–10': 0, '10–30': 1, '30–60': 2, '>60': 3}
}

# Dataset sesuai buku (disederhanakan dalam angka)
X = [
    [1, 0, 0, 1, 1, 2, 0, 1, 0, 0],
    [1, 0, 0, 1, 2, 0, 0, 0, 2, 2],
    [0, 1, 0, 0, 1, 0, 0, 0, 3, 0],
    [1, 0, 1, 1, 2, 0, 1, 0, 2, 1],
    [1, 0, 1, 0, 2, 2, 0, 1, 0, 3],
    [0, 1, 0, 1, 1, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 3, 0],
    [0, 0, 0, 1, 1, 1, 1, 1, 2, 0],
    [0, 1, 1, 0, 2, 0, 1, 0, 3, 3],
    [1, 1, 1, 1, 2, 2, 0, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 2, 0],
    [1, 1, 1, 1, 2, 0, 0, 0, 3, 2]
]

Y = [1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1]  # 1 = Yes, 0 = No

# Train decision tree
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)

# Fungsi GUI
def predict():
    input_data = [
        mapping['Alternate'][alt_var.get()],
        mapping['Bar'][bar_var.get()],
        mapping['Fri/Sat'][fri_var.get()],
        mapping['Hungry'][hungry_var.get()],
        mapping['Patrons'][patrons_var.get()],
        mapping['Price'][price_var.get()],
        mapping['Raining'][rain_var.get()],
        mapping['Reservation'][res_var.get()],
        mapping['Type'][type_var.get()],
        mapping['WaitEstimate'][wait_var.get()]
    ]
    result = clf.predict([input_data])
    result_label.config(text="Keputusan: Akan Menunggu" if result[0] == 1 else "Keputusan: Tidak Menunggu")

def show_tree():
    fig = plt.figure(figsize=(15,8))
    tree.plot_tree(clf, filled=True,
                   feature_names=list(mapping.keys()),
                   class_names=['No', 'Yes'])
    plt.show()

# GUI
root = tk.Tk()
root.title("Klasifikasi Menunggu Restoran - Decision Tree")

# Variabel input
alt_var = tk.StringVar(value='No')
bar_var = tk.StringVar(value='No')
fri_var = tk.StringVar(value='No')
hungry_var = tk.StringVar(value='No')
patrons_var = tk.StringVar(value='None')
price_var = tk.StringVar(value='$')
rain_var = tk.StringVar(value='No')
res_var = tk.StringVar(value='No')
type_var = tk.StringVar(value='Burger')
wait_var = tk.StringVar(value='0–10')

# Form
fields = [
    ('Alternate', alt_var, ['No', 'Yes']),
    ('Bar', bar_var, ['No', 'Yes']),
    ('Fri/Sat', fri_var, ['No', 'Yes']),
    ('Hungry', hungry_var, ['No', 'Yes']),
    ('Patrons', patrons_var, ['None', 'Some', 'Full']),
    ('Price', price_var, ['$', '$$', '$$$']),
    ('Raining', rain_var, ['No', 'Yes']),
    ('Reservation', res_var, ['No', 'Yes']),
    ('Type', type_var, ['French', 'Italian', 'Thai', 'Burger']),
    ('WaitEstimate', wait_var, ['0–10', '10–30', '30–60', '>60'])
]

for idx, (label, var, options) in enumerate(fields):
    tk.Label(root, text=label).grid(row=idx, column=0)
    tk.OptionMenu(root, var, *options).grid(row=idx, column=1)

tk.Button(root, text="Prediksi", command=predict).grid(row=11, column=0)
tk.Button(root, text="Lihat Pohon", command=show_tree).grid(row=11, column=1)

result_label = tk.Label(root, text="Keputusan:")
result_label.grid(row=12, columnspan=2)

root.mainloop()
