export const register = async ({
  username,
  password,
}: {
  username: string;
  password: string;
}) => {
  let response = await fetch("http://localhost:8000/user/create/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    credentials: "include",
    body: JSON.stringify({ username, password }),
  });

  return response;
};

export const login = async ({
  username,
  password,
}: {
  username: string;
  password: string;
}) => {
  let response = await fetch("http://localhost:8000/user/login/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "Authorization": `Bearer ${localStorage.getItem("jwt")}`
    },
    credentials: "include",
    body: JSON.stringify({ username, password }),
  });

  return response;
};
