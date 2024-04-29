import {Router} from "express"
import UserManager from "../controllers/UserManager.js"
import FinanceManager from "../controllers/FinanceManager.js";
const newFinanceManager=new FinanceManager("usersfinances.json","users.json")
const newUserManager=new UserManager('users.json');
const menuRouter=Router()

menuRouter.get("/:uid",async(req,res)=>{
    try {
        const {uid}=req.params
        const users=await newFinanceManager.readUsers();
        const usersFinances=await newFinanceManager.readFile();
        const user=users.find(user=>user.id===JSON.parse(uid));
        const finances=usersFinances.find(finance=>finance.id===JSON.parse(uid));
        const bills=finances.bills
        const incomes=finances.monthlyIncomes;
        res.render("menu",{user,finances,bills,incomes})
    } catch (error) {
        res.send(error)
    }
})

menuRouter.post("/getExpensesByCategory",async(req,res)=>{
    try {
        const {uid,value}=req.body
        console.log(uid,value)
        const result=await newFinanceManager.getTotalByCategory(JSON.parse(uid),value);
        res.send(result)
    } catch (error) {
        res.send(error)
    }
})
menuRouter.post("/getTotalExpenses",async(req,res)=>{
    try {
        const {uid}=req.body
        const result=await newFinanceManager.getTotalExpenses(JSON.parse(uid))
        res.send(result)
    } catch (error) {
        res.send(error)
    }
})
menuRouter.post("/getTotalIncomes",async(req,res)=>{
    try {
        const {uid}=req.body
        const result=await newFinanceManager.getTotalIncomes(JSON.parse(uid));
        res.send(result)
    } catch (error) {
        res.send(error)
    }
})
menuRouter.post("/newIncome",async(req,res)=>{
    try {
        const{uid,amount,description}=req.body
        const result=await newFinanceManager.addIncome(JSON.parse(uid),JSON.parse(amount),description)
        res.send(result)
    } catch (error) {
        res.send(error)
    }
})
menuRouter.post("/newExpense",async(req,res)=>{
    try {
        const{uid,amount,description,value}=req.body
        console.log(uid,amount,description,value)
        const result=await newFinanceManager.addExpense(JSON.parse(uid),JSON.parse(amount),value,description);
        console.log(result)
        res.send(result)
    } catch (error) {
        res.send(error)
    }
})
export default menuRouter