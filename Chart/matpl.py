import matplotlib.pyplot as plt
from datacenter.projectdb import PDataBase

db_controler = PDataBase()


class Matplot:
    def __init__(self) -> None:
        pass

    def plot_pie_charts(self, counts, username):
        if (
            "UserIncome" in counts
            and counts["UserIncome"] != 0
            and "UserCost" in counts
            and counts["UserCost"] != 0
        ):
            self.plot_combined_pie_chart(counts, username)
        elif "UserIncome" in counts and counts["UserIncome"] != 0:
            self.plot_income_pie_chart(counts, username)
        elif "UserCost" in counts and counts["UserCost"] != 0:
            self.plot_cost_pie_chart(counts, username)

    def plot_combined_pie_chart(self, counts, username):
        fig, axs = plt.subplots(3, 1, figsize=(10, 7.5))
        fig.suptitle("Charts", fontsize=16)
        counts["total_combined_count"] = db_controler.get_row_count_for_user_in_table(
            "UserIncome", username
        ) + db_controler.get_row_count_for_user_in_table("UserCost", username)
        sizes_combined = [
            counts["total"],
            counts["total_combined_count"] - counts["total"],
        ]
        colors = ["#ff9999", "#66b3ff"]
        labels_comb = ["Filtered Cost and Income", "Total"]
        axs[0].pie(sizes_combined, labels=labels_comb, autopct="%1.1f%%", colors=colors)
        axs[0].set_title("Combined Income and Cost Data")

        # Income Data
        counts["total_income_count"] = db_controler.get_row_count_for_user_in_table(
            "UserIncome", username
        )
        sizes_income = [
            counts["UserIncome"],
            counts["total_income_count"] - counts["UserIncome"],
        ]
        axs[1].pie(
            sizes_income,
            labels=["Filtered Income", "Total Income"],
            autopct="%1.1f%%",
            colors=colors,
        )
        axs[1].set_title("Income Data")

        # Expense Data
        counts["total_cost_count"] = db_controler.get_row_count_for_user_in_table(
            "UserCost", username
        )
        sizes_expense = [
            counts["UserCost"],
            counts["total_cost_count"] - counts["UserCost"],
        ]
        axs[2].pie(
            sizes_expense,
            labels=["Filtered Cost", "Total Cost"],
            autopct="%1.1f%%",
            colors=colors,
        )
        axs[2].set_title("Cost Data")

        plt.tight_layout()
        plt.show()

    def plot_income_pie_chart(self, counts, username):
        counts["total_income_count"] = db_controler.get_row_count_for_user_in_table(
            "UserIncome", username
        )
        sizes_income = [
            counts["UserIncome"],
            counts["total_income_count"] - counts["UserIncome"],
        ]
        colors = ["#ff9999", "#66b3ff"]
        labels_income = ["Filtered Income", "Total Income"]
        plt.pie(sizes_income, autopct="%1.1f%%", colors=colors)
        plt.title("Income Data")
        plt.show()

    def plot_cost_pie_chart(self, counts, username):
        counts["total_cost_count"] = db_controler.get_row_count_for_user_in_table(
            "UserCost", username
        )
        sizes_expense = [
            counts["UserCost"],
            counts["total_cost_count"] - counts["UserCost"],
        ]
        colors = ["#ff9999", "#66b3ff"]
        labels_cost = ["Filtered Cost", "Total Cost"]
        plt.pie(sizes_expense, autopct="%1.1f%%", colors=colors)
        plt.title("Expense Data")
        plt.show()
