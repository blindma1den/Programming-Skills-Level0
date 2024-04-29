import fs from "fs"

class PackageManager{
    constructor(packagePath,usersPath){
        this.path=packagePath,
        this.usersPath=usersPath
    }
    async readUsers(){
        try {
            const users=await fs.promises.readFile(this.usersPath,"utf-8")
            return JSON.parse(users)
        } catch (error) {
            if(error.code==="ENOENT"){
                return []
            }else{
                return error
            }
        }
    }
    async readPackages(){
        try {
            const packages=await fs.promises.readFile(this.path,"utf-8")
            return JSON.parse(packages)
        } catch (error) {
            if(error.code="ENOENT"){
                return []
            }else{
                return error
            }
        }
    }
    async sendPackage(id,sender,adress,destinatary,contactNumber,instructions="NO SE REGISTRARON INSTRUCCIONES"){
        try {
            const users=await this.readUsers();
            const user=users.find(user=>user.id===id)
            const packages=await this.readPackages();
            const SendNewPackage={
                sender:sender,
                destinatary:destinatary,
                adress:adress,
                contactNumber:contactNumber,
                instructions:instructions,
                id:await this.getNextId()
            }
            packages.push(SendNewPackage);
            if(packages.length>1)fs.unlinkSync(this.path)
            await fs.promises.writeFile(this.path,JSON.stringify(packages,null,"\t"),"utf-8");
            const newPackage={
                id:SendNewPackage.id,
                status:false,
                destinatary:destinatary
            }
            user.shipments.push(newPackage)
            await fs.promises.writeFile(this.usersPath,JSON.stringify(users,null,"\t"),"utf-8");
            const data={
                message:"package sent successfully",
                pid:SendNewPackage.id
            }
            return data
        } catch (error) {
            return error
        }
    }
    async getNextId(){
        let packages=await this.readPackages();
        if(packages==="ENOENT"||packages.length===0){
            return 1
        }else{ 
                console.log
                return packages[packages.length -1].id+1
        }
    }
    shippingPrice(weight){
        const price =weight*2
        const data={
            message:`Shipping Price will be USD ${price}`,
            amount:price,
        }
        return data
    }
    async getShipments(uid){
        try {
            const users=await this.readUsers()
            console.log(users)
            const user=users.find(user=>user.id===uid)
            const shipments=user.shipments
            if(shipments.length===0){
                const data={
                    message:'THERE IS NO SHIPMENTS YET',
                    shipments:0
                }
                return data
            }else{
                const shipmentsData=[]
                shipments.forEach(element => {
                    if(element.status===true){
                        const data={
                            message:`Sent to ${element.destinatary}`,
                            status:'Package Delivered',
                            shipmentCode:element.id
                        }
                        shipmentsData.push(data)
                        }else{
                            const data={
                                destinatary:`Sent to ${element.destinatary}`,
                                status:'Package on the way',
                                shipmentCode:element.id
                            }
                            shipmentsData.push(data)
                        }
                    
                });
                return shipmentsData
            }
        } catch (error) {
            return error
        }
    }
}
export default PackageManager