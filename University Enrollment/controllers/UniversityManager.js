import fs from 'fs'
import __dirname from "../utils.js"
class UniversityManager{
    constructor(path,users){
        this.path=__dirname+"/"+path;
        this.users=__dirname+"/"+users
    }
    async readFile(){
        try {
            const data =await fs.promises.readFile(this.path);
            return JSON.parse(data)
        } catch (error) {
            if(error.code==="ENOENT"){
                return []
            }else{
                console.log(error)
            }
        }
    }
    async readUsers(){
        try {
            const users=await fs.promises.readFile(this.users)
            return JSON.parse(users)
        } catch (error) {
            if(error.code==="ENOENT"){
                return []
            }else{
                console.log(error)
            }
        }
    }
    async addProgram(name){
        try {
            const programs=await this.readFile();
             const newProgram={
            name:name,
            slots:5,
            students:[],
            campus:[{name:"London",slots:1},{name:"Manchester",slots:3},{name:"Liverpool",slots:1}]
        }
            programs.push(newProgram);
            if(programs.lengt>1)fs.unlinkSync(this.path)
            await fs.promises.writeFile(this.path,JSON.stringify(programs,null,"\t"),"utf-8")
        } catch (error) {
            console.log(error)
        }
        
       
        
    }
    async userPickProgram(name,lastname,programName,campusName,username){
        try {
            const users=await this.readUsers();

            const programs= await this.readFile();
            const program=programs.find(program=>program.name===programName);
            if(program.slots===0){
                return ('THERE IS NOT SLOTS IN THIS PROGRAM')
            }else{
                const campus=program.campus.find(campus=>campus.name===campusName)
                //console.log(campus)
                if(campus.slots===0){
                    const campusWithSlot=[];
                    program.campus.forEach(element => {
                        if(element.slots > 0) {
                            campusWithSlot.push(element.name)
                        }
                    });
                    const data={
                        message:('There is no slots in this campus,try in '),
                        campus:campusWithSlot
                    }
                    return data
                }else{
                    const user=users.find(user=>user.username===username)
                    user.inProgram=true;
                    user.program=programName;               
                    await fs.promises.writeFile(this.users,JSON.stringify(users,null,"\t"),"utf-8")
                    const newStudent={name:name,lastname:lastname,campus:campusName,program:programName}
                    campus.slots--
                    program.slots--
                    program.students.push(newStudent)
                    await fs.promises.writeFile(this.path,JSON.stringify(programs,null,"\t"),"utf-8")
                    const data ={
                        message:"Successfull, Welcome to the camp",
                        username:user.username,
                        progra:programName
                    }
                    return data
                }
                
            }
        } catch (error) {
            return error
        }
    }

}
export default UniversityManager