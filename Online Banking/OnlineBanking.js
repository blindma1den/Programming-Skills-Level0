const fs=require('fs')
class OnlineBank{
    constructor(path){
        this.path=path
        this.balance=10000;
    }
    async readFile(){
        try {
            const users=await fs.promises.readFile(this.path,'utf-8')
            return JSON.parse(users)
        } catch (error) {
            if(error.code==="ENOENT"){
                return []
            }else{
                return error
            }
        }
        
    }
    async createUser(username,password){
        try {
             const users=await this.readFile();
            if(!username||!password){
                return ('you must fill all the data')
            }else{
                const user=users.some(user=>user.username===username);
                if(user){
                    console.log('USER NOT AVAILABLE')
                    return ('USER NOT AVAILABLE')
                }else{
                    const newUser={username:username,password:password,balance:2000,status:true,strike:0};
                    if(users.length>0)fs.unlinkSync(this.path); 
                    users.push(newUser);
                    await fs.promises.writeFile(this.path,JSON.stringify(users,null,"\t"),"utf-8");
                    this.balance=this.balance+2000;
                    return ('USER CREATED')       
                }
                }
        } catch (error) {
            return error
        }
       
    }
    async userValidate(username,password){
        try {
            const users=await this.readFile();
            const validateUsername=users.some(user=>user.username===username)
            if(validateUsername){
                const user=users.find(user=>user.username===username);
                const validatePassword=(user.password===password);
                if(user.status===false){
                    return null
                }
                if(validatePassword){
                    return true
                }else{
                    return false
                }
            }else{
                return false
            }
        } catch (error) {
            return error
        }
    }
    async userLogin(username,password){
        try {
            const users=await this.readFile();
            if(!username||!password){
                return ('you must fill all the data')
            }else{
                const validateUser=await this.userValidate(username,password);
                if(validateUser){
                    
                }
                const userToValidate=users.find(user=>user.username===username);
                if(!userToValidate){
                    return ('USER NOT FOUND')
                }else{
                    if(userToValidate.status===false){
                        return ('THIS USER IS BANNED,CONTACT WITH AND ADMIN')
                    }
                    else if(password===userToValidate.password){
                        console.log('user log in succesfully')
                        return (userToValidate)
                    }   else{
                        userToValidate.strike=userToValidate.strike+1
                        console.log(userToValidate.strike)
                        if(userToValidate.strike===3){
                            userToValidate.status=false
                            await fs.promises.writeFile(this.path,JSON.stringify(users,null,"\t"),"utf-8");
                            return ('USER HAS BEEN BANNED,CONCTACT WITH AN ADMIN')
                        }
                        else{
                            await fs.promises.writeFile(this.path,JSON.stringify(users,null,"\t"),"utf-8");
                            console.log(`USER STRIKE: ${userToValidate.strike}`)
                            return(`WRONG PASSWORD STRIKE:${userToValidate.strike}`) 
                        }
                    }
                }
            }
        } catch (error) {
            return error
        }
    }
    async userViewBalance(username,password){
        try {
            const user=await newBanking.userLogin(username,password);
            if(user.balance){
                return (`Your balance is : ${user.balance}$`)
            }else{
                return user
            }
        } catch (error) {
            return error
        }
        
    }
    async userTransfer(username1,password,username2,number){
        try {
            const users=await this.readFile();
            const validate=await this.userValidate(username1,password);
            console.log(validate)
            if(validate){
                const user=users.find(user=>user.username===username1);
                if(user.balance<number){
                    return ('insuficents founds')
                }else{
                    const userToTransfer=users.find(user=>user.username===username2);
                    
                    if(userToTransfer!==user){
                        if(userToTransfer.status===false){
                            return('This user is banned,transfer rejected')
                        }else{
                            userToTransfer.balance=userToTransfer.balance+number
                            user.balance=user.balance-number
                            await fs.promises.writeFile(this.path,JSON.stringify(users,null,"\t"),"utf-8");
                            return (`Succesfull transfer,your balance is : ${user.balance}`)
                        }
                        
                    }else{
                        return('U cant transfer to yourself')
                    }
                }
            }else{
                return ('you must validate your user first')
            }
        } catch (error) {
            return error
        }
    }
    async userDeposit(username,password,number){
        try {
            const validate=await this.userValidate(username,password);
            if(validate){
                const users=await this.readFile();
                const user=users.find(user=>user.username===username);
                user.balance=user.balance+number;
                await fs.promises.writeFile(this.path,JSON.stringify(users,null,"\t"),"utf-8");
                this.balance=this.balance+number
                return ("Succesfull Deposit")
            }else{
                return ('you must validate your user first')
            }
        } catch (error) {
            return error
        }
    }
    async userWithdraw(username,password,number){
        try {
            const validate=await this.userValidate(username,password);
            if(validate){
                const users=await this.readFile();
                const user=users.find(user=>user.username===username);
                user.balance=user.balance-number;
                await fs.promises.writeFile(this.path,JSON.stringify(users,null,"\t"),"utf-8");
                this.balance=this.balance-number
                return ("Succesfull Withdraw")
            }else{
                return ('you must validate your user first')
            }
        } catch (error) {
            return error
        }
    }
    bankGetBalance(){
        return (`BANK BALANCE IS : ${this.balance}$`)
    }
}
const newBanking=new OnlineBank("users.json");



const myFunction=async ()=>{
    const results=await newBanking.createUser("momo","apa");
    console.log(results) 
    const results2=newBanking.bankGetBalance();
    console.log(results2)
}
myFunction();
//"goosisca122"