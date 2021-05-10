import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import mplcursors

from src.salary_calculator import SalaryCalculator
from src.disposable_income import DisposableIncome

Pension_Contribution = 0.05

# Create df with all combo of salary
salary_range = list(range(50000, 105000, 5000))
person_1 = salary_range * len(salary_range)
person_2 = sorted(person_1)

salary_matrix = pd.DataFrame({"person_1": person_1, "person_2": person_2})

glasgow_save = []
london_save = []
person_1_takehome = {}

for index, row in salary_matrix.iterrows():
    person_1_takehome_g = SalaryCalculator(
        row[0], "G", Pension_Contribution
    ).take_home()
    person_2_takehome_g = SalaryCalculator(
        row[1], "G", Pension_Contribution
    ).take_home()
    monthly_takehome_g = (person_1_takehome_g + person_2_takehome_g) / 12

    person_1_takehome_l = SalaryCalculator(
        row[0], "L", Pension_Contribution
    ).take_home()
    person_2_takehome_l = SalaryCalculator(
        row[1], "L", Pension_Contribution
    ).take_home()
    monthly_takehome_l = (person_1_takehome_l + person_2_takehome_l) / 12

    glasgow = DisposableIncome(795, 264, 125, 40, 225, 160, 150)
    london = DisposableIncome(1400, 264, 180, 40, 350, 200, 350)

    glasgow_save.append(glasgow.disposable_income(monthly_takehome_g))
    london_save.append(london.disposable_income(monthly_takehome_l))

#london_save = [None if i < min(glasgow_save) else i for i in london_save]

salary_matrix["save_invest_glasgow"] = glasgow_save
salary_matrix["save_invest_london"] = london_save

sns_data_glasgow = result = salary_matrix.pivot(
    index="person_1", columns="person_2", values="save_invest_glasgow"
)
sns_data_london = result = salary_matrix.pivot(
    index="person_1", columns="person_2", values="save_invest_london"
)

# min returns None
plot_min = min(filter(lambda x: x is not None, glasgow_save + london_save))
plot_max = max(filter(lambda x: x is not None, glasgow_save + london_save))
#mask = np.triu(np.ones_like(sns_data_glasgow, dtype=np.bool), k=1)
fig, ax = plt.subplots(1, 2)
sns.heatmap(
    sns_data_glasgow,
    annot=False,
    fmt="g",
    cmap="YlGnBu",
    ax=ax[0],
    vmax=plot_max,
    vmin=plot_min
    # mask=mask,
)
sns.heatmap(
    sns_data_london,
    annot=False,
    fmt="g",
    cmap="YlGnBu",
    ax=ax[1],
    vmax=plot_max,
    vmin=plot_min
    # mask=mask,
)

ax[0].invert_yaxis()
ax[1].invert_yaxis()

ax[0].set_title("saves + invest - Glasgow")
ax[1].set_title("saves + invest - London")

plt.tight_layout()
#plt.savefig("compare_save_invest.png", dpi=400)

mplcursors.cursor(hover=True)
plt.show()
