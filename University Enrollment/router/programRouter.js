import {Router}from 'express'
import UserManager from '../controllers/UserManager.js'
import UniversityManager from '../controllers/UniversityManager.js';
const newUniversityManager=new UniversityManager('programs.json',"users.json")
const newUserManager=new UserManager("users.json");
const programRouter=Router();

programRouter.get('/:programName/:username',async (req,res)=>{
    try {
        const {programName,username}=req.params
        const programs=await newUniversityManager.readFile();
        const programData=programs.find(program=>program.name===programName)
        const users=await newUserManager.readFile();
        const userData=users.find(user=>user.username===username);
        res.render('program',{program:programData,user:userData})
    } catch (error) {
        
    }
})

export default programRouter