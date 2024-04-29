import {Router} from "express"
import UserManager from "../controllers/UserManager.js"
const newUserManager=new UserManager("users.json")
const userRouter=Router();

userRouter.get('/',(req,res)=>{
    try {
        res.render('login',{})
    } catch (error) {
        res.send(error);
    }
})
userRouter.get('/register',(req,res)=>{
    try {
        res.render('register',{})
    } catch (error) {
        res.send(error);
    }
})
userRouter.post('/login',async (req,res)=>{
    try {
        const {username,password}=req.body
        const results=await newUserManager.userValidate(username,password)
        res.send(results)
    } catch (error) {
        res.send(error);
    }
})
userRouter.post('/register',async(req,res)=>{
    try {
        const {username,password,name,lastname}=req.body
        const results =await newUserManager.createUser(username,password,name,lastname)
        res.send(results);
    } catch (error) {
        res.send(error);
    }
})

export default userRouter