import {Router} from "express"
import UserManager from "../controllers/UserManager.js"
import PackageManager from "../controllers/PackageManager.js";
const newPackageManager=new PackageManager("packages.json","users.json")
const newUserManager=new UserManager("users.json")
const menuRouter=Router();


menuRouter.get('/:uid',async(req,res)=>{
    try {
        const {uid}=req.params
        const users=await newUserManager.readFile();
        console.log(users)
        const user=users.find(user=>user.id===JSON.parse(uid));
        console.log(user)
        res.render("menu",{user:user})
    } catch (error) {
        res.send(error)
    }
})
menuRouter.post('/getShipments',async(req,res)=>{
    try {
        const {uid}=req.body
        const results=await newPackageManager.getShipments(JSON.parse(uid))
        console.log(results)
        res.send(results)
    } catch (error) {
        res.send(error)
    }
})
menuRouter.post('/getShippingPrice',(req,res)=>{
    try {
        const {weigth}=req.body
        const results=newPackageManager.shippingPrice(JSON.parse(weigth))
        console.log(results)
        res.send(results)
    } catch (error) {
        res.send(error)
    }
    
})
menuRouter.get('/sendPackage/:uid',async(req,res)=>{
    try {
        const {uid}=req.params;
        const users=await newUserManager.readFile();
        const user=users.find(user=>user.id===JSON.parse(uid))
        res.render("sendPackage",{user:user})
    } catch (error) {
        res.send(error)
    }
})
menuRouter.post('/sendPackage',async(req,res)=>{
    try {
        const {uid,sender,receiver,address,contact,instructions}=req.body
        const results=await newPackageManager.sendPackage(JSON.parse(uid),sender,address,receiver,contact,instructions)
        res.send(results)
    } catch (error) {
        res.send(error)
    }
})

export default menuRouter