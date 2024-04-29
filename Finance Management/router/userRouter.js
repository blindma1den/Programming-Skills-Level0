import {Router} from "express"
import UserManager from "../controllers/UserManager.js"
import FinanceManager from "../controllers/FinanceManager.js";
const newFinanceManager=new FinanceManager("usersfinances.json","users.json")
const newUserManager=new UserManager('users.json');
const userRouter=Router();

userRouter.get('/',(req,res)=>{
    try {
        res.render('login',{})
    } catch (error) {
        res.send(error)
    }
})
userRouter.get('/register',(req,res)=>{
    try {
        res.render('register',{})
    } catch (error) {
        res.send(error)
    }
})
userRouter.post('/register',async(req,res)=>{
    try {
        const {name,lastname,password,username,email}=req.body
        const result=await newUserManager.createUser(name,lastname,email,username,password)
        console.log(result)
        res.send(result)
    } catch (error) {
        res.send(error)
    }
})
userRouter.post("/login",async(req,res)=>{
    try {
        console.log(req.body)
        const {username,password}=req.body
        const result=await newUserManager.validateUser(username,password)
        console.log(result)
        res.send(result)
    } catch (error) {
        res.send(error)
    }
})
userRouter.get('/registerIncomes/:uid',async(req,res)=>{
    try {
        const {uid}=req.params
        const users=await newUserManager.readFile()
        const user=users.find(user=>user.id===JSON.parse(uid))
        res.render("registerIncomes",{user:user})
        
    } catch (error) {
        res.send(error)
    }
})
userRouter.post("/initialBalance",async (req,res)=>{
    try {
        const {uid,monthlyIncome,monthlyIncomeDescription,education,educationDescription,entertainmentDescription,entertainment,medicalDescription,medical,savings,savingsDescription,homeExpenses,homeExpensesDescription}=req.body
        const expenses={
            education:JSON.parse(education),
            educationDescription:educationDescription,
            entertainment:JSON.parse(entertainment),
            entertainmentDescription:entertainmentDescription,
            medical:JSON.parse(medical),
            medicalDescription:medicalDescription,
            savings:JSON.parse(savings),
            savingsDescription:savingsDescription,
            homeExpenses:JSON.parse(homeExpenses),
            homeExpensesDescription:homeExpensesDescription
        }
        const monthly_incomes={
            amount:JSON.parse(monthlyIncome),
            description:monthlyIncomeDescription
        }
        const results=await newFinanceManager.updateFinance(JSON.parse(uid),monthly_incomes,expenses)
        console.log(results)
        res.send(results)
    } catch (error) {
        res.send(error)
    }
})
export default userRouter