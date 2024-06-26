import Link from "next/link";
import MaxWidthWrapper from "./MaxWidthWrapper";
import { GithubIcon, Phone } from "lucide-react";

const Footer = () => {
  return (
    <footer className="w-full bg-black text-white mt-20">
      <MaxWidthWrapper className="flex flex-col md:flex-row justify-between py-6">
        <section>
          <h3 className="text-2xl text-primary font-semibold">FastFood</h3>
          <p className="text-sm mt-2">
            Taste the real flavor in your city, just by some clicks.
          </p>
          <div className="flex flex-col mt-4 space-y-2">
            <Link className="text-primary" href={"#"}>
              About us
            </Link>
            <Link className="text-primary" href={"#"}>
              Locations
            </Link>
            <p className="flex gap-x-2">
              <Phone className="w-4" /> +52 01 800 123 4567
            </p>
          </div>
        </section>
        <section className="flex flex-col mt-10 md:mt-0 md:items-end">
          <h3 className="text-2xl text-primary font-semibold">
            Example project
          </h3>
          <p className="text-sm mt-2">
            This project was made to improve our skills in web development.
          </p>
          <div className="flex flex-col mt-4 space-y-2 md:text-right">
            <Link className="text-primary" href={"#"}>
              ExalGithub / Backend
            </Link>
            <Link className="text-primary" href={"#"}>
              NNeshz / Frontend
            </Link>
            <Link href={"#"} className="flex gap-2">
              <GithubIcon className="w-4" /> Github Repository
            </Link>
          </div>
        </section>
      </MaxWidthWrapper>
    </footer>
  );
};

export default Footer;
