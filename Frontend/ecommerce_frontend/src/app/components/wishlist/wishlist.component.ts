import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { EcommerceService } from 'src/app/services/ecommerce.service';

@Component({
  selector: 'app-wishlist',
  templateUrl: './wishlist.component.html',
  styleUrls: ['./wishlist.component.css']
})
export class wishlistComponent implements OnInit {
  wishlist:any
  product:any
  constructor(private service:EcommerceService,private router:Router) { }

  ngOnInit(): void {
    
    this.service.wishlistListservice().then(res=>res.json()).then(data=>{this.wishlist=data,console.log(data),this.product=data.product
    })
  }
  placeOrderwishlistFunction(id:any){
    localStorage.setItem("id",id)
    this.router.navigateByUrl('place-order')
  }
  removeFromwishlistFunction(id:any){
    this.service.removeFromwishlistService(id).then(res=>res.json()).then(data=>console.log(data))
    setTimeout(location.reload.bind(location), 1000)
  }
}
