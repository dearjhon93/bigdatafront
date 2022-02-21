import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class VuelosRutasClimaService {

  public baseUrl = "http://127.0.0.1:5000/consulta3/2007";
  constructor(private httpClient: HttpClient) { }

  public getVuelos(): Observable<any> {
    return this.httpClient.get(`${this.baseUrl}`);
  }
}
