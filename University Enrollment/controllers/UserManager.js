import fs from 'fs';

class UserManager{
    constructor(path){
        this.path=path;
    }
    async readFile(){
        try {
            const users=await fs.promises.readFile(this.path,"utf-8");
            return JSON.parse(users)
            
        } catch (error) {
            if(error.code==="ENOENT"){
                return []
            }else{
                return error
            }
        }
    }
    async createUser(username,password,name,lastname){
        try {
            const users=await this.readFile();
            const validateUsername=users.some(user=>user.username===username);
            if(validateUsername){
                return ('USERNAME ALREADY USED,TRY ANOTHER')
            }else{
                const newUser={
                    username:username,
                    password:password,
                    name:name,
                    lastname:lastname,
                    loginFailed:0,
                    status:true,
                    program:"",
                    inProgram:false                   
                }
                users.push(newUser);
                if(users.length>1) fs.unlinkSync(this.path);
                await fs.promises.writeFile(this.path,JSON.stringify(users,null,"\t"),"utf-8");
                return 'USER HAS BEEN CREATED SUCCESSFULLY'
            }
        } catch (error) {
            console.log(error);
        }
    }
    async userValidate(username,password){
        try {
            const users=await this.readFile();
            const user=users.find(user=>user.username===username)
            if(!user){
                return('THERE IS NO USER REGISTERED WITH THE INPUTED USERNAME')
            }else{
                if (user.status===false){
                    return ('THIS USER IS BANNED,CONTACT WIHT AN ADMIN')
                }else{
                    if(user.password===password){
                        return user
                    }else{
                        user.loginFailed=user.loginFailed+1
                        if(user.loginFailed===3){
                            user.status=false
                            await fs.promises.writeFile(this.path,JSON.stringify(users,null,"\t"),"utf-8");
                            return ('WRONG PASSWORD 3 TIMES,YOUR USER HAS BEEN BANNED')
                        }else{
                            await fs.promises.writeFile(this.path,JSON.stringify(users,null,"\t"),"utf-8");
                            return(`WRONG PASSWORD,U HAVE ${3-user.loginFailed} MORE TRYS`)
                        }
                    }
                }
            }
        } catch (error) {
            return error
        }
    }
}
export default UserManager