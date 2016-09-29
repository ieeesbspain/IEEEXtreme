/*
 * Copyright (C) 2014 MineCoders
 *
 * This program is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public License
 * as published by the Free Software Foundation; either version 3
 * of the License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
 */

import java.util.ArrayList;
import java.util.Comparator;
import java.util.LinkedList;
import java.util.List;
import java.util.ListIterator;
import java.util.PriorityQueue;
import java.util.Scanner;

/**
 * Segundo problema de IEEEXtreme 8.0.
 */
public class Solution {
    
    public static void main(String[] args) {
        // Parse la entrada
        Scanner scanner = new Scanner(System.in);
        
        // Tamaño del mapa
        int len = scanner.nextInt();
        int[][] mapa = new int[len][len];
        
        // Cada línea es una fila
        for (int i = 0; i < len * len; i++) {
            mapa[i / len][i % len] = scanner.nextInt();
        }
        
        // Creamos el escenario y el pathfinding
        Escenario escenario = new Escenario(mapa);
        Pathfinding pathfinding = new Pathfinding(escenario);
        
        // Vamos probando por cada destino posible
        int minCoste = Integer.MAX_VALUE;
        for (int i = 0; i < len; i++) {
            for (int j = 0; j < len; j++) {
                Punto origen = new Punto(0, j);
                Punto destino = new Punto(len - 1, i);
                int coste = pathfinding.calculateFrom(origen, destino);

                // System.out.print("RUTA(" + coste + "):");
                // while (pathfinding.iterator().hasNext())
                //     System.out.print(pathfinding.iterator().next() + " ");
                // System.out.println();

                if (coste < minCoste)
                    minCoste = coste;
            }
        }
        
        System.out.println(minCoste);
    }
    
    private static class Escenario {
        private final int[][] mapa;
        
        public Escenario(final int[][] mapa) {
            this.mapa = mapa;
        }

        public int getWidth() {
            return this.mapa.length;
        }
        
        public int getHeight() {
            return this.mapa[0].length;
        }
        
        public int getCoste(int x, int y) {
            return this.mapa[y][x];
        }
    }
    
    /**
     * Representa un punto en el espacio de dos dimensiones.
     */
    private static class Punto implements Comparable<Punto> {
        /** Coordenada X. */
        private final int x;

        /** Coordenada Y. */
        private final int y;

        /**
         * Crea una nueva instancia de punto.
         * 
         * @param x Coordenada X.
         * @param y Coordenada Y.
         */
        public Punto(final int x, final int y) {
            this.x = x;
            this.y = y;
        }

        /**
         * Obtiene la coordenada X.
         * 
         * @return Coordenada X.
         */
        public int getX() {
            return this.x;
        }

        /**
         * Obtiene la coordenada Y.
         * 
         * @return Coordenada Y.
         */
        public int getY() {
            return this.y;
        }

        /**
         * Obtiene una nuevo punto desplazado del actual.
         * 
         * @param dx Desplazamiento en X.
         * @param dy Desplazamiento en Y.
         * @return Nuevo punto desplazado.
         */
        public Punto offset(final int dx, final int dy) {
            return new Punto(this.getX() + dx, this.getY() + dy);
        }

        /**
         * Obtiene la distancia entre este punto y otro.
         * 
         * @param pt2 Segundo punto en la distancia.
         * @return Distancia entre puntos.
         */
        public double distancia(final Punto pt2) {
            return Math.sqrt(
                    (this.getX() - pt2.getX()) * (this.getX() - pt2.getX()) +
                    (this.getY() - pt2.getY()) * (this.getY() - pt2.getY())
            );
        }

        @Override
        public int compareTo(Punto o) {
            int cmp = Integer.compare(this.getX(), o.getX());
            if (cmp == 0)
                cmp = Integer.compare(this.getY(), o.getY());

            return cmp;
        }

        @Override
        public int hashCode() {
            int hash = 3;
            hash = 83 * hash + this.x;
            hash = 83 * hash + this.y;
            return hash;
        }

        @Override
        public boolean equals(Object obj) {
            if (obj == null) {
                return false;
            }
            if (getClass() != obj.getClass()) {
                return false;
            }
            final Punto other = (Punto) obj;
            if (this.x != other.x) {
                return false;
            }
            if (this.y != other.y) {
                return false;
            }
            return true;
        }

        @Override
        public String toString() {
            return "[" + (this.x + 1) + ", " + (this.y + 1) + "]";
        }
        
        
    }

    /**
    * Algoritmo A* de pathfinding para la vuelta de los fantasmas a su jaula.
    */
   private static class Pathfinding {
       /** Ruta final. */
       private final LinkedList<Punto> ruta;

       /** Iterador de la ruta final. */
       private ListIterator<Punto> iterador;

       /** Escenario actual. */
       private final Escenario escenario;

       /**
        * Crea una nueva instancia del algoritmo.
        * 
        * @param escenario Escenario de juego.
        */
       public Pathfinding(final Escenario escenario) {
           this.ruta = new LinkedList<>();
           this.escenario = escenario;
       }

       /**
        * Limpia la ruta encontrada.
        */
       public void clear() {
           this.ruta.clear();
       }

       /**
        * Calcula una nueva ruta desde la posición dada usando el algoritmo A*.
        * 
        * @param origen Posición de partida.
        */
       public int calculateFrom(final Punto origen, final Punto destino) {
           PriorityQueue<PointData> openList = new PriorityQueue<>(1, new PointDataComparator());
           List<PointData> closeList = new ArrayList<>();

           // 0.- Añado la celda origen a la lista abierta
           int costeOrigen = this.escenario.getCoste(origen.getX(), origen.getY());
           openList.offer(new PointData(origen, null, destino, costeOrigen));

           do {
               // 1.- Cojo el primer elemento de la lista y lo pongo en la cerrada
               PointData ptData = openList.poll();
               closeList.add(ptData);

               // 2.- Busco las celdas adyacentes a la extraída
               List<Punto> adyacentes = new ArrayList<>(4);
               adyacentes.add(ptData.coord.offset(+1, 00));
               adyacentes.add(ptData.coord.offset(-1, 00));
               adyacentes.add(ptData.coord.offset(00, +1));
               adyacentes.add(ptData.coord.offset(00, -1));

               // 3.- Por cada adyacente...
               for (Punto pt : adyacentes) {                   
                   // A) Comprobar que sea una posición válida
                   if (pt.getX() < 0 || pt.getX() >= this.escenario.getWidth())
                       continue;

                   if (pt.getY() < 0 || pt.getY() >= this.escenario.getHeight())
                       continue;
                   
                   // B) Comprobar si es el destino -> hemos acabado
                   int ptCoste = this.escenario.getCoste(pt.getX(), pt.getY());
                   if (pt.equals(destino)) {
                       closeList.add(ptData.creaHijo(pt, ptCoste));
                       this.reconstruyeRuta(closeList);
                       return ptCoste + ptData.getCosteG();
                   }

                   // C) Si ya está en la lista cerrada, adiós
                   boolean contiene = false;
                   for (int i = 0; i < closeList.size() && !contiene; i++)
                       if (closeList.get(i).getCoord().equals(pt))
                           contiene = true;

                   if (contiene)
                       continue;

                   // D) Comprobamos si está en la lista abierta y actualiza si eso
                   int tentativaCoste = ptData.getCosteG() + ptCoste;
                   contiene = false;
                   for (PointData ptOpen : openList) {
                       // Ya estaba incluida
                       if (ptOpen.getCoord().equals(pt)) {                     
                           // Se puede mejorar
                           if (tentativaCoste < ptOpen.getCosteG())
                               ptOpen.update(ptData);

                           contiene = true;
                           break;
                       }
                   }

                   if (contiene)
                       continue;

                   // E) Añadimos a la lista abierta
                   openList.add(ptData.creaHijo(pt, ptCoste));
               }

               // 4.- Ordenar la lista abierta por coste. Se hace automáticamente.
               // 5.- Volver a (1)
           } while (!openList.isEmpty());

           // ERROR
           System.err.println("Error en A*");
           return Integer.MAX_VALUE;
       }

       /**
        * Reconstruye la ruta a partir de la salida del algoritmo A*.
        * 
        * @param closeList Lista cerrada.
        */
       private void reconstruyeRuta(final List<PointData> closeList) {
           // Obtiene el destino y lo añade a la ruta
           PointData nodo = closeList.get(closeList.size() - 1);
           this.ruta.clear();

           // Mientras haya padres, navegar
           do {
               this.ruta.addFirst(nodo.coord);
               nodo = nodo.padre;
           } while (nodo.padre != null);
           
           // Añade el origen
           this.ruta.addFirst(nodo.coord);

           this.iterador = this.ruta.listIterator();
       }

       /**
        * Obtiene el iterador de la ruta.
        * 
        * @return Iterador de la ruta.
        */
       public ListIterator<Punto> iterator() {
           return this.iterador;
       }

       /**
        * Punto del escenario con datos para el algoritmo A*.
        */
       private static class PointData {
           /** Coordenada que representa. */
           private final Punto coord;

           /** Punto de destino del algoritmo. */
           private final Punto dst;

           /** Coste G. */
           private int costeG;

           /** Coste H. */
           private int costeH;

           /** Punto padre del algoritmo. */
           private PointData padre;

           /**
            * Crea una nueva instancia.
            * 
            * @param coord Coordenada que representa.
            * @param padre Coordenada padre de la que se ha llegado.
            * @param dst Coordenada de destino.
            */
           public PointData(Punto coord, PointData padre, Punto dst, int coste) {
               this.coord  = coord;
               this.dst    = dst;
               this.padre  = padre;
               this.costeG = coste + ((padre == null) ? 0 : padre.getCosteG());
               this.updateCosteH();
           }

           /**
            * Obtiene la coordenada que representa.
            * 
            * @return Coordenada.
            */
           public Punto getCoord() {
               return this.coord;
           }

           /**
            * Obtiene el coste G.
            * 
            * @return Coste G.
            */
           public int getCosteG() {
               return costeG;
           }

           /**
            * Obtiene el coste H.
            * 
            * @return Coste H.
            */
           public int getCosteH() {
               return costeH;
           }

           /**
            * Obtiene el coste F.
            * 
            * @return Coste F.
            */
           public int getCosteF() {
               return this.costeG + this.costeH;
           }

           /**
            * Obtiene el punto padre.
            * 
            * @return Punto padre.
            */
           public PointData getPadre() {
               return padre;
           }

           /**
            * Actualiza el coste a partir del nuevo padre.
            * 
            * @param padre Nuevo padre.
            */
           public void update(PointData padre) {
               this.padre  = padre;
               this.costeG = padre.getCosteG() + 1;
               this.updateCosteH();
           }

           /**
            * Recalcula el coste H.
            */
           private void updateCosteH() {
               this.costeH = Math.abs(this.dst.getX() - this.coord.getX()) + 
                             Math.abs(this.dst.getY() - this.coord.getY());
           }

           /**
            * Crea un punto hijo para la coordenada dada.
            * 
            * @param coord Coordenada del nuevo punto.
            * @return Punto hijo.
            */
           public PointData creaHijo(Punto coord, int coste) {
               return new PointData(coord, this, this.dst, coste);
           }
       }

       /**
        * Comparador de puntos para A*.
        */
       private static class PointDataComparator implements Comparator<PointData> {
           @Override
           public int compare(PointData pt1, PointData pt2) {
               int cmp = Integer.compare(pt1.getCosteF(), pt2.getCosteF());
               if (cmp == 0)
                   cmp = pt1.getCoord().compareTo(pt2.getCoord());

               return cmp; 
           }
       }
   }

}
