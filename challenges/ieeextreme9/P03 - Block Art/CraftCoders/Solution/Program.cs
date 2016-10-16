//
//  Program.cs
//
//  Author:
//       IEEE Student Branch of Granada
//
//  Copyright (c) 2015 IEEE Student Branch of Granada (c) 2015
//
//  This program is free software: you can redistribute it and/or modify
//  it under the terms of the GNU General Public License as published by
//  the Free Software Foundation, either version 3 of the License, or
//  (at your option) any later version.
//
//  This program is distributed in the hope that it will be useful,
//  but WITHOUT ANY WARRANTY; without even the implied warranty of
//  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
//  GNU General Public License for more details.
//
//  You should have received a copy of the GNU General Public License
//  along with this program.  If not, see <http://www.gnu.org/licenses/>.
using System;
using System.Linq;
using System.Collections.Generic;
using System.Collections;

namespace Solution
{
    public class MainClass
    {
        public static void Main()
        {
            // Read dimensions - Not used.
            Console.ReadLine().Split(' ');

            // Create the list of layers.
            List<Layer> layers = new List<Layer>();

            // Get number of queries
            int numQueries = Convert.ToInt32(Console.ReadLine());
            for (int i = 0; i < numQueries; i++) {
                Query query = Query.FromString(Console.ReadLine());
                ProcessQuery(layers, query);
            }
        }

        private static void ProcessQuery(List<Layer> layers, Query query)
        {
            switch (query.Operation) {
            case Operations.Add:
            case Operations.Remove:
                layers.Add(query.Layer);
                break;

            case Operations.Question:
                ShowLayer(layers, query.Layer);
                break;
            }
        }

        private static void ShowLayer(List<Layer> layers, Layer queryLayer)
        {
            int count = 0;
            foreach (Layer layer in layers)
                count += layer.Value * layer.IntersectedArea(queryLayer);

            Console.WriteLine(count);
        }
    }

    public class Layer
    {
        public Layer(int value, Point start, Point end)
        {
            Value = value;
            Start = start;
            End = end;
        }

        public int Value {
            get;
            set;
        }

        public int Left {
            get { return Start.X; }
        }

        public int Right {
            get { return End.X; }
        }

        public int Top {
            get { return Start.Y; }
        }

        public int Bottom {
            get { return End.Y; }
        }

        public Point Start {
            get;
            private set;
        }

        public Point End {
            get;
            private set;
        }

        public bool Intersect(Layer rect)
        {
            return this.Left <= rect.Right && this.Right >= rect.Left &&
                this.Top <= rect.Bottom && this.Bottom >= rect.Top;
        }

        public int IntersectedArea(Layer rect)
        {
            if (!Intersect(rect))
                return 0;

            int intersectedLeft   = Math.Max(this.Left, rect.Left);
            int intersectedRight  = Math.Min(this.Right, rect.Right);
            int intersectedTop    = Math.Max(this.Top, rect.Top);
            int intersectedBottom = Math.Min(this.Bottom, rect.Bottom);
            return (intersectedRight - intersectedLeft   + 1) *
                (intersectedBottom - intersectedTop + 1);
        }

        public override string ToString()
        {
            return string.Format("[Layer: Value={0}, Start={1}, End={2}]", Value, Start, End);
        }
    }

    public class Query
    {
        public Query(Operations operation, Point start, Point end)
        {
            Operation = operation;
            Start = start;
            End = end;
        }

        public Operations Operation {
            get;
            private set;
        }

        public Point Start {
            get;
            private set;
        }

        public Point End {
            get;
            private set;
        }

        public Layer Layer {
            get {
                return new Layer((int)Operation, Start, End);
            }
        }

        public static Query FromString(string data)
        {
            string[] args = data.Split(' ');

            Operations operation = Operations.Add;
            switch (args[0]) {
            case "a":
                operation = Operations.Add;
                break;

            case "r":
                operation = Operations.Remove;
                break;

            case "q":
                operation = Operations.Question;
                break;
            }

            Point start = new Point(
                              Convert.ToInt32(args[2]) - 1,
                              Convert.ToInt32(args[1]) - 1);
            Point end = new Point(
                Convert.ToInt32(args[4]) - 1,
                Convert.ToInt32(args[3]) - 1);

            return new Query(operation, start, end);
        }

        public override string ToString()
        {
            return string.Format("[Query: Operation={0}, Start={1}, End={2}]", Operation, Start, End);
        }
    }

    public enum Operations {
        Add = 1,
        Remove = -1,
        Question = 0
    }

    public class Point
    {
        public Point(int x, int y)
        {
            X = x;
            Y = y;
        }

        public int X {
            get;
            private set;
        }

        public int Y {
            get;
            private set;
        }

        public override string ToString()
        {
            return string.Format("[Point: X={0}, Y={1}]", X, Y);
        }
    }
}
