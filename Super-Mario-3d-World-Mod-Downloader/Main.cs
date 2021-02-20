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
            Process.Start("CMD.exe","curl -L "+link+" -o output.zip").WaitForExit();
            Directory.CreateDirectory("Copy");
            ZipFile.ExtractToDirectory("output.zip", "Copy");
            File.Delete("output.zip");
            Console.WriteLine("Enter the region you want to install for.\n[1] USA\n[2] EUR\n[3] JPN\n");
            string choice = Console.ReadLine();
            if (choice == "1")
            {
                goto USA;
            }
            else if (choice == "2")
            {
                //pass for now
            }
            else if (choice == "3")
            {
                //pass for now
            }
            else
            {
                Environment.Exit(1);
            }
        USA:
            Console.WriteLine("Enter the drive letter of your SD card;");
            string drive = Console.ReadLine();
            string cwd = Directory.GetCurrentDirectory();
            Directory.SetCurrentDirectory(drive);
            if (Directory.Exists("sdcafiine") == true)
            {
                Directory.SetCurrentDirectory("sdcafiine");
            } else
            {
                Directory.CreateDirectory("sdcaffine");
                Directory.SetCurrentDirectory("sdcafiine");
            }
        }
    }
}
