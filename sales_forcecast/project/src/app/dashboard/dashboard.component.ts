import { Component, OnInit } from '@angular/core';
import { AuthService } from '../_services/auth.service';

import { HttpClient } from '@angular/common/http';
@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {
  selectedDay:string="";
  service: any;
  data: any;
  per ="";
  c = "";
 

  file:any;
  formdata: any;
  formData:FormData=new FormData;
  
  update(){
    var  f=<HTMLInputElement>(document.getElementById("formFile"));
    if(f.files){
   this.file=f.files[0]
    }
  }
 

  selectChangeHandler(event:any){
    this.selectedDay=event.target.value;
    // this.formdata.append('String',this.selectedDay);
  }

  logout(){
    //remove token
    this.auth.removeToken();
    this.auth.canAccess();
}

  constructor(private auth:AuthService, private http:HttpClient) { }
  user = {localId:"someid",displayName:"somename"};
  ngOnInit(): void {
    this.auth.canAccess();
    if (this.auth.isAuthenticated()) {
        //call user details service
        this.auth.detail().subscribe({
          next:data=>{
              this.user.localId = data.users[0].localId;
              this.user.displayName = data.users[0].displayName;
          }
        })
    }
  }

  upload()
  {
    
    
    this.formData.append ('file',this.file);
    this.formData.append ('per',this.per);
    this.formData.append ('c',this.c);
    console.log(this.formData.get);
    this.auth.upload(this.formData).subscribe((data: any) =>{
      console.log(data);
      console.log('data');
      
    },
    error =>console.log(error)
    );

  }


}