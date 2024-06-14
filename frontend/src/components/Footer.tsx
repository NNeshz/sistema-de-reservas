import { Github } from "lucide-react";
import Link from "next/link";

const Footer = () => {
  return (
    <footer className="rounded-lg w-full bg-yellow-400 text-white text-center py-4 px-8 flex items-center justify-between">
      <p> &copy; 2024 All rights reserved</p>
      <div>
        This project was created by{" "}
        <Link href={"https://github.com/ExalGitHub"} className="text-black font-semibold">ExalGithub</Link> &&{" "}
        <Link href={"/https://github.com/NNeshz"} className="text-black font-semibold">NNeshz</Link>
      </div>
    </footer>
  );
};

export default Footer;
