import { Component, OnInit } from '@angular/core';
import { RetrasoPorAerolinea } from 'src/app/modelos/retraso-aero';
import { VuelosAerolineasService } from 'src/app/servicios/vuelos-aerolineas.service';

@Component({
  selector: 'app-por-aerolinea',
  templateUrl: './por-aerolinea.component.html',
  styleUrls: ['./por-aerolinea.component.css']
})
export class PorAerolineaComponent implements OnInit {

  vuelos: RetrasoPorAerolinea[]= [];
  public page = 1; // página actual
  public pageSize = 150; // número de páginas
  public maxSize = 10;

  constructor(private vuelosAeroService: VuelosAerolineasService) { }

  ngOnInit(): void {
    this.vuelosAeroService.getVuelos().subscribe(respuesta=>{
      console.log(respuesta);
      this.vuelos=respuesta;
    });
  }  

}
