export const signIn = async ({
  username,
  password,
}: {
  username: string;
  password: string;
}) => {
  await fetch("http://localhost:8000/user/create/", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    credentials: "include",
    body: JSON.stringify({ username, password }),
  })

  console.log("User created");
};
