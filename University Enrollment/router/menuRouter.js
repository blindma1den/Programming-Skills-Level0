import {Router}from 'express'
import UserManager from '../controllers/UserManager.js'
import UniversityManager from '../controllers/UniversityManager.js';
const newUniversityManager=new UniversityManager('programs.json',"users.json")
const newUserManager=new UserManager("users.json");
const menuRouter=Router();

menuRouter.get('/:username',async(req,res)=>{
    try {
        const {username}=req.params
        const users=await newUserManager.readFile();
        const user=users.find(user=>user.username===username);
        console.log(user)
        res.render('menu',{user:user})
    } catch (error) {
        
    }
})
menuRouter.post('/registerProgram',async(req,res)=>{
    try {
        const {program,name,lastname,campus,username}=req.body
        const results=await newUniversityManager.userPickProgram(name,lastname,program,campus,username);
        console.log(results)
        res.send(results)
    } catch (error) {
            res.send(error);
    }
})
export default menuRouter