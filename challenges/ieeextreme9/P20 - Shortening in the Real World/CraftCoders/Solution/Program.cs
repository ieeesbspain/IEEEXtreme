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

namespace Solution
{
    public class MainClass
    {
        private static System.Text.Encoding Encoding = System.Text.Encoding.UTF8;
        private static readonly char[] Alphabet = new char[62];

        public static void Main()
        {
            for (int i = 0; i < 10; i++)
                Alphabet[i] = (char)('0' + (i - 00));
            for (int i = 10; i <= 35; i++)
                Alphabet[i] = (char)('a' + (i - 10));
            for (int i = 36; i <= 61; i++)
                Alphabet[i] = (char)('A' + (i - 36));

            string baseUrl = Console.ReadLine();

            int numUrls = Convert.ToInt32(Console.ReadLine());
            for (int i = 0; i < numUrls; i++)
                Console.WriteLine(EncodeUrl(baseUrl, Console.ReadLine()));
        }

        private static string EncodeUrl(string baseUrl, string finalUrl)
        {
            // First get the string bytes
            byte[] baseBytes = Encoding.GetBytes(baseUrl);
            byte[] finalBytes = Encoding.GetBytes(finalUrl);

            // XOR Encode with the base URL
            for (int i = 0; i < finalBytes.Length; i++)
                finalBytes[i] ^= baseBytes[i % baseBytes.Length];

            // Get the last 8 bytes and convert to ulong
            ulong lowerBytes = BitConverter.ToUInt64(
                finalBytes.Reverse().ToArray(),
                0);

            // Encode the integer with Base62
            string base62Encoded = Base62Encoding(lowerBytes);

            return baseUrl + '/' + base62Encoded;
        }

        private static string Base62Encoding(ulong value)
        {
            string encoded = string.Empty;
            ulong alphabetLength = (ulong)Alphabet.Length;
            do {
                encoded = Alphabet[value % alphabetLength] + encoded;
                value /= alphabetLength;
            } while (value != 0);

            return encoded;
        }

    }
}
