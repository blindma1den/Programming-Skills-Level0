import {Router} from 'express';
import UserManager from '../controllers/UserManager.js';
const newUserManager=new UserManager("users.json");
const homeRouter=Router();

homeRouter.get('/',(req,res)=>{
    try {
        res.render('home',{});
    } catch (error) {
        res.send(error)
    }
})
homeRouter.get('/register',(req,res)=>{
    try {
        res.render('register',{})
    } catch (error) {
        res.send(error);
    }
})
homeRouter.post('/login',async (req,res)=>{
    try {
        const {username,password}=req.body
        const users=await newUserManager.readFile();
        const results=await newUserManager.userValidate(username,password);
        res.send(results)
    } catch (error) {
        res.send(error);
    }
})
homeRouter.post('/register',async(req,res)=>{
    console.log("aaa")
    try {
        const {name,lastname,username,password}=req.body;
        const results=await newUserManager.createUser(username,password,name,lastname)
        console.log(results)
        res.send(results)
    } catch (error) {
        res.send(error)
    }
})
/*
homeRouter.get('/menu/:username',async(req,res)=>{
    try {
        const users=newUserManager.readFile();
        const user=users.find(user=>user.username===username);
        res.render('menu',{user:user})
    } catch (error) {
        
    }
})
*/

export default homeRouter