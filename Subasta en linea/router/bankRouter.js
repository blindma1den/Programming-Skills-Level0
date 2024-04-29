import {Router} from "express"
const currencyRouter=Router();
import { CurrencyBank } from "../controllers/CurrencyBank.js"
const currencyBank=new CurrencyBank("users.json","exchangerates.json");

currencyRouter.get('/',(req,res)=>{
    try {
        res.render('bank')
    } catch (error) {
        res.send(error);
    }
})
currencyRouter.post('/createUser',async(req,res)=>{
    try {
        const {username,password}=req.body
        const users=await currencyBank.readFile();
        const createUser=await currencyBank.createUser(username,password)
        if(createUser===false){
            res.send(false)
        }
        else if(createUser===true){
            res.send(createUser)
        }
    } catch (error) {
        res.send(error)
    }
})
currencyRouter.post('/login',async(req,res)=>{
    try {
        const {username,password}=req.body;
        const loginResults=await currencyBank.validateUser(username,password)
        res.send(JSON.stringify(loginResults))
    } catch (error) {
        res.send(error)
    }
})
currencyRouter.get('/currencyMenu/:username',async(req,res)=>{
    try {
        const {username}=req.params
        const users=await currencyBank.readFile();
        const user=users.find(user=>user.username===username);
        
        res.render('currencyMenu',{user:user})
    } catch (error) {
        res.send(error);
    }
})
currencyRouter.put('/currencyMenu',async(req,res)=>{
    try {
        const {a,b,username,amount}=req.body
        console.log(a,b,amount,username)
        const results=await currencyBank.exchange(a,b,amount,username);
        console.log(results)
        res.send(results)
    } catch (error) {
        res.send(error)
    }
})
currencyRouter.put('/currencyMenu/withdraw',async(req,res)=>{
    try {
        const{coin,username,amount}=req.body;
        //console.log(coin,username,amount)
        const results=await currencyBank.withdraw(amount,username,coin);
        res.send(results)
    } catch (error) {
        res.send(error)
    }
})
//currencyBank.createUser("Gonzalo","Casimiro")
export default currencyRouter

