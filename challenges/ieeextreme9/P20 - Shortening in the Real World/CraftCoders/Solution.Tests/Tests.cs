//
//  Test.cs
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
using System.Collections;
using NUnit.Framework;
using System;
using System.IO;
using System.Text;
using System.Reflection;

namespace Solution.Tests
{
    [TestFixture]
    public class Tests
    {
        private string[,] publicCases;

        public Tests()
        {
            // By default they will be in the solution directory
            TestFilesPath = Path.Combine(
                Path.GetDirectoryName(Assembly.GetExecutingAssembly().Location),
                "../../../");

            FindTestFiles();
        }

        public string TestFilesPath {
            get;
            set;
        }

        public IEnumerable PublicCases {
            get {
                for (int i = 0; i < publicCases.GetLength(0); i++) {
                    if (publicCases[i, 0] == null)
                        continue;
                    
                    yield return new TestCaseData(publicCases[i, 0])
                        .Returns(publicCases[i, 1]);
                }
            }
        }

        [Test, TestCaseSource("PublicCases")]
        public string TestPublicCases(string input)
        {
            return TestSolution(input);
        }

        protected string TestSolution(string input)
        {
            // Save the standard input and output for restoring later.
            var stdIn = Console.In;
            var stdOut = Console.Out;

            // Redirect the output writing to a StringBuilder.
            var output = new StringBuilder();
            var redirectedOutput = new StringWriter(output);
            Console.SetOut(redirectedOutput);

            // Redirect the input reading from the string.
            var redirectedInput = new StringReader(input);
            Console.SetIn(redirectedInput);

            // Call our program.
            MainClass.Main();

            // Restore input and output.
            Console.SetIn(stdIn);
            Console.SetOut(stdOut);

            // Return output
            return output.ToString();
        }


        private void FindTestFiles()
        {
            var inputs = Directory.GetFiles(TestFilesPath, "input*.txt");

            publicCases = new string[inputs.Length, 2];
            foreach (string inputFile in inputs) {
                string filename = Path.GetFileNameWithoutExtension(inputFile);
                string num = filename.Substring(5, 2);

                string outputFile = Path.Combine(TestFilesPath,
                    "output" + num + ".txt");
                if (!File.Exists(outputFile))
                    continue;

                int idx = Convert.ToInt32(num) - 1;
                publicCases[idx, 0] = File.ReadAllText(inputFile);
                publicCases[idx, 1] = File.ReadAllText(outputFile);
            }
        }
    }
}

