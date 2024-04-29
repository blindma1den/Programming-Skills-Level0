import fs from "fs"
class UserManager{
    constructor(path){
        this.path=path;
    }
    async readFile(){
        try {
            const users=await fs.promises.readFile(this.path,"utf-8")
            return JSON.parse(users)
        } catch (error) {
            if(error.code==="ENOENT"){
                return []
            }else{
                return error
            }
        }
    }
    async createUser(name,lastname,email,username,password){
        try {
            const users=await this.readFile(this.path,"utf-8");
            const validateUsername=users.some(user=>user.username===username);
            if(validateUsername){
                const data={
                    message:"USERNAME ALREADY USED,TRY ANOTHER",
                    status:null,
                }
                return  data
            }else{
                const newUser={
                    username:username,
                    password:password,
                    name:name,
                    lastname:lastname,
                    email:email,
                    loginFailed:0,
                    status:true,
                    id:await this.getNextId(),
                    monthlyIncome:false
                }
                users.push(newUser);
                if(users.length>1)fs.unlinkSync(this.path);
                await fs.promises.writeFile(this.path,JSON.stringify(users,null,'\t'),"utf-8");
                const data={
                    message:"USER HAS BEEN CREATED SUCCESSFULLY",
                    status:true
                }
                return data
            }

        } catch (error) {
            return error
        }
    }
    async validateUser(username,password){
        try {
            const users=await this.readFile();
            const user=users.find(user=>user.username===username);
            if(!user){
                const data={
                    message:"THERE IS NO USER REGISTERED WITH THE INPUTED USERNAME",
                    status:null
                }
                return data
            }else{
                if(user.status===false){
                    const data={
                        message:"THIS USER IS BANNED,CONCATC WITH AN ADMIN",
                        status:false
                    }
                    return data
                }else{
                    if(user.password===password){
                        return user
                    }else{
                        user.loginFailed=user.loginFailed+1
                        if(user.loginFailed===3){
                            user.status=false
                            await fs.promises.writeFile(this.path,JSON.stringify(users,null,"\t"),"utf-8")
                            const data={
                                message:"WRONG PASSWORD 3 TIMES,YOUR USER HAS BEEN BANNED",
                                status:false
                            }
                            return data
                        }else{
                            await fs.promises.writeFile(this.path,JSON.stringify(users,null,"\t"),"utf-8")
                            const data={
                                message:`WRONG PASSWORD, U HAVE ${3-user.loginFailed} MORE TRYS`,
                                status:null
                            }
                            return data
                        }
                    }
                }
            }
        } catch (error) {
            return error
        }
    }
    async getNextId(){
        let products=await this.readFile();
        if(products==="ENOENT"||products.length===0){
            return 1
        }else{ 
                console.log
                return products[products.length -1].id+1
        }
    }
}
export default UserManager