"use client"

import { usePathname } from "next/navigation";

const CategoryProductPage = () => {
  const pathname = usePathname();
  console.log(pathname);

  return (
    <div>
      <h1>Category Product Page</h1>
    </div>
  );
};

export default CategoryProductPage;
