import fs from "fs"

class FinanceManager{
    constructor(path,users){
        this.path=path
        this.users=users
    }
    async readFile(){
        try {
            const usersFinances =await fs.promises.readFile(this.path,"utf-8")
            return JSON.parse(usersFinances)
        } catch (error) {
            if(error.code==="ENOENT"){
                return []
            }else{
                return error
            }
        }
    }
    async readUsers(){
        try {
            const users=await fs.promises.readFile(this.users,"utf-8")
            return JSON.parse(users)
        } catch (error) {
            if(error.code==="ENOENT"){
                return []
            }else{
                return error
            }
        }
    }
    async updateFinance(uid,monthlyIncomes,expenses){
        console.log(uid)
        try {
            const users=await this.readUsers()
            console.log(users)
            const user=users.find(user=>user.id===uid)
            const usersFinances=await this.readFile();
            const newFinance={
                balance:null,
                status:null,
                id:uid,
                monthlyIncomes:[
                    {description:monthlyIncomes.description,
                    amount:monthlyIncomes.amount}
                    ],
                bills:{
                    medical:[{
                        description:expenses.medicalDescription,
                        amount:expenses.medical
                        }],
                    homespends:[{
                        description:expenses.homeExpensesDescription,
                        amount:expenses.homeExpenses
                    }],
                    leisure:[{
                        description:expenses.entertainmentDescription,
                        amount:expenses.entertainment
                    }],
                    saving:[{
                        description:expenses.savingsDescription,
                        amount:expenses.savings
                    }],
                    education:[{
                        description:expenses.educationDescription,
                        amount:expenses.education
                    }]
                }
            }
            const totalExpenses=expenses.medical+expenses.homeExpenses+expenses.entertainment+expenses.savings+expenses.education
            const amountMax=Math.max(expenses.medical,expenses.homeExpenses,expenses.entertainment,expenses.savings,expenses.education
                    )
                    console.log(amountMax)
            const from=Object.keys(newFinance.bills).find(key => {
                const bill = newFinance.bills[key][0];
                return bill.amount === amountMax;
            })
            const biggestDescription=newFinance.bills[from][0].description
            newFinance.balance={
                amount:monthlyIncomes.amount-totalExpenses,
                biggestExpense:{
                    amount:amountMax,
                    from:Object.keys(newFinance.bills).find(key => {
                        const bill = newFinance.bills[key][0];
                        return bill.amount === amountMax;
                    }),
                    description:biggestDescription
                }
            }
            if(newFinance.balance<totalExpenses)newFinance.status=false;
            if(newFinance.balance>totalExpenses)newFinance.status=true;
            if(newFinance.balance===totalExpenses)newFinance.status=null;
            usersFinances.push(newFinance);
            if(usersFinances.length>1) fs.unlinkSync(this.path)
            await fs.promises.writeFile(this.path,JSON.stringify(usersFinances,null,"\t"),"utf-8");

            const data={
                message:"Succesfully registration",
                status:true
            }
            user.monthlyIncome=true;
            await fs.promises.writeFile(this.users,JSON.stringify(users,null,"\t"),"utf-8");
            return data
        } catch (error) {
            return error
        }   

    }
    async getTotalByCategory(uid,category){
        try {
            const users=await this.readUsers();
            const usersFinances=await this.readFile();
            const userFinance=usersFinances.find(finance=>finance.id===uid);
            const financeCategory=userFinance.bills[category];
            let total=0
            financeCategory.forEach(element => {
                total=total+element.amount
            });
            const data={
                message:`The total of the amount of ${category} expenses is : ${total}`,
                amount:total
            }
            return data
        } catch (error) {
            return error
        }
    }
    async getTotalExpenses (uid){
        try {
            const users=await this.readUsers()
            const user=users.find(user=>user.id===uid);
            const finances=await this.readFile()
            const finance=finances.find(finance=>finance.id===uid);
            const bills=finance.bills
            let total=0
            for (const category in bills) {
                if (bills.hasOwnProperty(category)) {
                    const categoryExpenses = bills[category];
                    categoryExpenses.forEach(expense => {
                        total += expense.amount;
                    });
                }
            }
            const data={
                message:`The total of all expenses is : ${total}`,
                total:total
            }
            return data

        } catch (error) {
            return error
        }
    }
    async getTotalIncomes(uid){
        try {
            const finances=await this.readFile()
            const finance=finances.find(finance=>finance.id===uid);
            const incomes=finance.monthlyIncomes
            let total=0
            incomes.forEach(element=>{
                total=total+element.amount
            })
            const data={
                message:`The total of all incomes is : ${total}`,
                total:total
            }
            return data
        } catch (error) {
            return error
        }
    }
    async addExpense(uid,amount,category,description){
        try {
            const usersFinances=await this.readFile();
            const userFinance=usersFinances.find(finance=>finance.id===uid)
            const newExpense={
                description:description,
                amount:amount
            }
            userFinance.bills[category].push(newExpense)
            userFinance.balance.amount=userFinance.balance.amount-amount
            if(newExpense.amount>userFinance.balance.biggestExpense.amount){
                userFinance.balance.biggestExpense.amount=amount;
                userFinance.balance.biggestExpense.from=category;
                userFinance.balance.biggestExpense.description=description;
            }
            fs.unlinkSync(this.path);
            await fs.promises.writeFile(this.path,JSON.stringify(usersFinances,null,"\t"),"utf-8")
            const data={
                message:`NEW EXPENSE HAS BEEN ADDED,YOUR BALANCE IS : ${userFinance.balance.amount}`,
                status:true
            }
            return data

        } catch (error) {
            return error
        }
    }
    async addIncome(uid,amount,description){
        try {
            const finances=await this.readFile();
        const finance=finances.find(finance=>finance.id===uid);
        const incomes=finance.monthlyIncomes
        const newIncome={
            description:description,
            amount:amount
        }
        incomes.push(newIncome);
        finance.balance.amount=finance.balance.amount+amount
        fs.unlinkSync(this.path);
        await fs.promises.writeFile(this.path,JSON.stringify(finances,null,"\t"),"utf-8");
        const data={
            message:`a new income has been added, your new balance is :${finance.balance.amount}`,
            status:true
        }
        
        return data
        } catch (error) {
           return error 
        }
        
    }
}
export default FinanceManager