// 5. Develop a finance management application with the following features:
// * 		The user records their total income.
// * 		There are categories: Medical expenses, household expenses, leisure, savings, and education.
// * 		The user can list their expenses within the categories and get the total for each category.
// * 		The user can obtain the total of their expenses.
// * 		If the user spends the same amount of money they earn,
//          the system should display a message advising the user to reduce expenses in the category
//          where they have spent the most money.
// * 		If the user spends less than they earn, the system displays a congratulatory message on the screen.
// * 		If the user spends more than they earn, the system will display advice to improve the user's financial health.

/*
El usuario pone sus ingresos.
Luego debe ingresar cuanto gasta en: Medical Expenses, HouseHold Expenses, Leisure, Savings, Education
Dentro de cada categoría puede poner en que se le va de esa categoría la guita
Al final obtiene el total x categoria y el total de gastos.
Si el usuario gasta lo mismo que genera, el sistema le aconsejará que reduzca sus gastos en la categoría que mas gasto.
Si el usuario gasta menos de lo que genera, el sistema lo felicitará.
Si el usuario gasta mas de lo que genera, el sistema le dará un consejo para mejorar su salud financiera.

HTML: 
*/

const incomesInput = document.getElementById('incomes-input');
const incomeButton = document.getElementById('incomes-button');
const expensesSelect = document.getElementById('expenses-select');
const expenseDescInput = document.getElementById('expense-description-input');
const expenseAmountInput = document.getElementById('expense-amount-input');
const expenseButton = document.getElementById('add-expense-button');
const finishButton = document.getElementById('finish-button');
let incomes = 0;
const expenses = {
  Medical: [],
  HouseHold: [],
  Leisure: [],
  Savings: [],
  Education: [],
};

const getIncomes = () => {
  const incomes = incomesInput.value;
  incomesInput.disabled = true;
  incomeButton.disabled = true;
  return incomes;
};

incomeButton.addEventListener('click', () => {
  incomes = Number(getIncomes());
  expenseButton.disabled = false;
});

expenseButton.addEventListener('click', () => {
  const newExpense = {
    description: expenseDescInput.value,
    amount: Number(expenseAmountInput.value),
  };
  expenses[expensesSelect.value].push(newExpense);
  expenseDescInput.value = '';
  expenseAmountInput.value = '';
  finishButton.disabled = false;
});

const getTotalExpensesByCategory = (category) => {
  let total = 0;
  expenses[category].forEach((expense) => {
    total += expense.amount;
  });
  return total;
};
let totalExpensesSum = 0;
let maxAmountCategory = {
  totalExpenses: 0,
  category: '',
};
const totalExpenses = () => {
  Object.keys(expenses).forEach((category) => {
    const totalExpenses = getTotalExpensesByCategory(category);

    if (totalExpenses > maxAmountCategory.totalExpenses) {
      maxAmountCategory = { totalExpenses, category };
    }
    console.log(`Total spent on ${category}: $${totalExpenses}`);
    return (totalExpensesSum = totalExpensesSum + totalExpenses);
  });
  expenseButton.disabled = true;
  console.log(`You are spent $ ${totalExpensesSum} in total `);
  console.log(`Your incomes are: $ ${incomes}`);
  const balance = incomes - totalExpensesSum;
  console.log(`Your balance is: $ ${balance}`);
  if (balance < 0) {
    console.log('You are in debt and need to save money!');
    console.log(
      `You have the biggest expense in: ${maxAmountCategory.category} with $ ${maxAmountCategory.totalExpenses}\n Maybe you should cut back on those expenses.  Or get a new job, bruh. `
    );
  } else if (balance == 0) {
    console.log('You are even!, but be careful');
  } else {
    console.log('You are doing great!');
  }
};

finishButton.addEventListener('click', totalExpenses);
