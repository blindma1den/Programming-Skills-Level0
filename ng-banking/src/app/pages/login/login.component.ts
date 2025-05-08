import { Component } from '@angular/core';
import { UserDTO} from '../../models/user'
import Swal from 'sweetalert2'
import { FormBuilder} from '@angular/forms'
import { Router } from '@angular/router';
import { ReactiveFormsModule } from '@angular/forms';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [ReactiveFormsModule],
  templateUrl: './login.component.html',
  styleUrl: './login.component.css'
})
export class LoginComponent {
  public listUsers:UserDTO[] = [];


  constructor( private router: Router,
               private fb:FormBuilder
               ){
    this.addUserSystem(this.createUserSystem());
    console.log('****************************')
    console.log(this.listUsers[0].username);
    console.log(this.listUsers[0].password);

  }

  public loginForm = this.fb.group(
    {
      username:'',
      password:''
    }
  )

  login(){
    if (this.loginUser()){

    }
    else {
      if(this.listUsers[0].times >=4){
        Swal.fire('Error','Usuario bloqueado','error')
      }else{
        Swal.fire('Error','Usuario no registrado','error')
      }

  }
  }


  loginUser():boolean{
    if((this.loginForm.value.username === this.listUsers[0].username)&&(this.loginForm.value.password === this.listUsers[0].password)){
        return true;
     }
    else{
      this.listUsers[0].times +=1;
      return false;
    }

  }

  createUserSystem():UserDTO{
    const user:UserDTO = {
      username : 'user1',
      password : 'pass1',
      times : 0
    }
    return user;
  }

  addUserSystem(user:UserDTO){
    this.listUsers.push(user);
  }

}
