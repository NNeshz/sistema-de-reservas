import Link from "next/link";
import MaxWidthWrapper from "./MaxWidthWrapper";

const Footer = () => {
  return (
    <footer className="w-full bg-yellow-400 text-xs text-black text-center py-2 md:py-4 md:text-sm px-8">
      <MaxWidthWrapper className="flex flex-col md:flex-row items-center justify-between">
        <p>&copy; 2024 All rights reserved</p>
        <div className="mt-1 md:mt-0">
          This project was created by{" "}
          <Link
            href="https://github.com/ExalGitHub"
            className="text-black font-semibold"
            target="_blank"
          >
            ExalGithub
          </Link>{" "}
          and{" "}
          <Link
            href="https://github.com/NNeshz"
            className="text-black font-semibold"
            target="_blank"
          >
            NNeshz
          </Link>
        </div>
      </MaxWidthWrapper>
    </footer>
  );
};

export default Footer;
