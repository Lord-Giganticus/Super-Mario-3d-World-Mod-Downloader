using System;
using System.Diagnostics;
using System.IO;
using System.IO.Compression;
using _3DW_Keys;

namespace Super_Mario_3d_World_Mod_Downloader
{
    class Program
    {
        public string USA_Key = USA.key;
        public string EUR_Key = EUR.key;
        public string JPN_Key = JPN.key;
        static void Main()
        {
            Console.WriteLine("Enter the 3DW Gamebanana download link you want to install for:");
            string link = Console.ReadLine();
            Environment.CurrentDirectory = Directory.GetCurrentDirectory();
            Process.Start("CMD.exe","curl -L "+link+" -o output.zip");
            ZipFile.ExtractToDirectory("output.zip", Directory.GetCurrentDirectory());
            File.Delete("output.zip");
        }
    }
}
