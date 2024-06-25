import Link from "next/link";
import MaxWidthWrapper from "./MaxWidthWrapper";

const Footer = () => {
  return (
    <footer className="w-full border-t">
      <MaxWidthWrapper className="flex justify-between py-2">
        <h3>Todos los derechos reservados</h3>
        <span>
          Created by <Link href={"#"} className="text-yellow-500 font-semibold">ExalGithub</Link> and{" "}
          <Link href={"#"} className="text-yellow-500 font-semibold">NNeshz</Link>
        </span>
      </MaxWidthWrapper>
    </footer>
  );
};

export default Footer;
