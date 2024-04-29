import fs from "fs";
import __dirname from "../util.js";
class CurrencyBank{
    constructor(path,ratesPath){
        this.path=__dirname+"/"+path
        this.ratesPath=__dirname+"/"+ratesPath
        this.bankBalance=0
    }
    async exchangeRates(){
        try {
            const exchangeRates=await fs.promises.readFile(this.ratesPath,"utf-8")
            return JSON.parse(exchangeRates)
        } catch (error) {
            return error
        }
    }
    async readFile(){
        try {
            const users=await fs.promises.readFile(this.path,"utf-8")
            return JSON.parse(users);
        }catch(error){
            if(error.code==="ENOENT"){
                return []
            }
            else{
                console.log(error);
            }
        }
    }
    async createUser(username,password){
        try {
            const users=await this.readFile();
            const userExists=users.some(user=>user.username===username);
            if(userExists){
                return (false)
            }else{
                const newUser={
                    username:username,
                    password:password,
                    wallet:{
                        USD:1156,
                        EUR:1060,
                        ARS:1000000,
                        CLP:978870,
                        TRY:37270,
                        GBP:912
                    }
                }
                users.push(newUser);
                if(users.length>1) fs.unlinkSync(this.path);
                await fs.promises.writeFile(this.path,JSON.stringify(users,null,"\t"),"utf-8");
                console.log("USUARIO CREADO,ESTO DEVUELVE TRUE")
                return (true);
            }
        } catch (error) {
            return error
        }
    }
    async validateUser(username,password){
        try {
            const users=await this.readFile();
            const validateUsername=users.some(user=>user.username===username);
            if(validateUsername){
                const user=users.find(user=>user.username===username);
                const validatePassword=user.password===password
                if(validatePassword){
                    return user   //passowrd correcto,devuelvo el user
                }else{
                    return ('Password Incorrecto')   //password incorrecto
                }
            }else{
                return ("EL USERNAME INGRESADO NO EXISTE")// NO EXISTE USER CON EL USERNAME INGREADO,DEVUELVO NULL
            }
        }
         catch (error) {
            return (error);
        }
    } 
    async exchange(coinA,coinB,quantity,username){
        try {
            const exchangeRates=await this.exchangeRates();
            const users=await this.readFile()
            const user=users.find(user=>user.username===username);
            console.log(user)
            let quantityA=user.wallet[coinA]
            let quantityB=user.wallet[coinB]
            const exchangeRate=exchangeRates[coinA][coinB]
            
            if(quantity>exchangeRates[coinA].LIMIT
            ||quantity<exchangeRates[coinA].MIN){
                console.log("A")
                return(`El MONTO MINIMO ES: ${exchangeRates[coinA].MIN} Y EL MAXIMO ES:${exchangeRates[coinA].LIMIT}`)
            }
            else if(quantity>quantityA){
                console.log("B")
                return ('NO TIENES ESA CANTIDAD EN TU WALLET')
            }
            else{
                console.log(quantity)
                console.log(exchangeRate)
                const results=exchangeRate*quantity
                console.log(results)
                user.wallet[coinA]=user.wallet[coinA]-quantity
                user.wallet[coinB]=user.wallet[coinB]+(Math.round(results))
                //console.log(user.wallet[coinA])
                //console.log(user.wallet[coinB])
                await fs.promises.writeFile(this.path,JSON.stringify(users,null,"\t"),"utf-8")
                return (`Intercambio exitoso`
                )
            }
        } catch (error) {
            return error
        }
    }
    async withdraw(amount,username,coin){
        //console.log(amount,username,coin)
        const users=await this.readFile();
        const user=users.find(user=>user.username===username);
        const coinBalance=user.wallet[coin];
        if(amount>coinBalance){
            return ('Fondos insuficentes para el monto ingresado')
        }else{
            user.wallet[coin]=user.wallet[coin]-amount;
            await fs.promises.writeFile(this.path,JSON.stringify(users,null,"\t"),"utf-8")
            const comision=amount/100*1
            const finalAmount=amount-comision
            const receipt={
                netWithdraw:amount,
                comision:comision,
                finalAmount:finalAmount
            }
            this.bankBalance=this.bankBalance+comision
            console.log(receipt)
            return receipt
        }
    }
}

export {CurrencyBank}

const currencyBank=new CurrencyBank("users.json","exchangerates.json");
//currencyBank.createUser("Gonzalo","Casimiro")

//currencyBank.exchange("USD", "ARS", 200, "Gonzalo")
  