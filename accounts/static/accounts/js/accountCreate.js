$(document).ready(function () {
  document.querySelector("#modal_create").onclick = function () {
    $(".coupled").modal({
      allowMultiple: true,
    });
    // open second modal if "+" button is clicked
    $(".parent_create")
      .modal("attach events", ".account_create .plus-icon")
      .modal({
        onDeny: function () {
          $(".parent_create").hide();
        },
        onApprove: function () {
          errorMessageParent.style.removeProperty("display");
          $("#parent").submit();
          return false;
        },
      });

    // Div for error messages
    const errorMessageParent = document.querySelectorAll(".error.message")[1];
    errorMessageParent.innerHTML == "";

    const errorMessageAccount = document.querySelectorAll(".error.message")[0];
    errorMessageAccount.innerHTML == "";

    const csrftoken = document.querySelector("[name=csrfmiddlewaretoken]").value;

    // Submit parent form
    document.getElementById("parent").onsubmit = function () {
      if (window.getComputedStyle(errorMessageParent).display === "none") {
        fetch("/api/parents/", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrftoken,
          },

          body: JSON.stringify({
            name: document.getElementById("id_parent-name").value,
            category: document.getElementById("id_parent-category").value,
            is_active: document.getElementById("id_parent-is_active").checked,
            credentials: "same-origin",
          }),
        }).then(response => {
          if (response.ok) {
            return response.json().then(result => {
              const option = document.createElement("option");
              option.text = result.name;
              option.value = result.id;
              option.selected = true;

              const drop = document.getElementById("id_account-parent_account");
              drop.add(option);
              document.querySelector(".ui.mini.modal").classList.remove("transition", "visible", "active");
              document.querySelector(".ui.mini.modal").style.display = "none";
            });
          } else {
            return response.json().then(result => {
              errorMessageParent.innerHTML = "";
              const errorList = document.createElement("ul");
              errorMessageParent.appendChild(errorList);
              const error = document.createElement("li");
              if (result.name) {
                error.innerHTML = result.name[0];
                errorList.classList.add("list");
                errorList.appendChild(error);
                errorMessageParent.style.setProperty("display", "block");
              }
            });
          }
        });
      }
      return false;
    };

    document.getElementById("account").onsubmit = function () {
      if (window.getComputedStyle(errorMessageAccount).display === "none") {
        let contacts = [];
        for (let option of document.getElementById("id_account-contacts").options) {
          if (option.selected) {
            contacts.push(option.value);
          }
        }

        fetch("/api/accounts/", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrftoken,
          },

          body: JSON.stringify({
            name: document.getElementById("id_account-name").value,
            country: document.getElementById("id_account-country").value,
            industry: document.getElementById("id_account-industry").value,
            status: document.getElementById("id_account-status").value,
            address: document.getElementById("id_account-address").value,
            website: document.getElementById("id_account-website").value,
            parent_account: document.getElementById("id_account-parent_account").value,
            assigned_to: document.getElementById("id_account-assigned_to").value,
            contacts: contacts,
            description: document.getElementById("id_account-description").value,
            is_active: document.getElementById("id_parent-is_active").checked,
            credentials: "same-origin",
          }),
        }).then(response => {
          if (response.ok) {
            return response.json().then(() => {
              const modal = document.querySelector(".ui.dimmer.modals");
              modal.classList.remove("transition", "visible", "active");
              modal.style.display = "none";

              const successMessage = document.querySelector(".success.message");
              successMessage.style.display = "block";

              setTimeout(function () {
                location.reload();
              }, 2000);
            });
          } else {
            return response.json().then(result => {
              errorMessageAccount.innerHTML = "";
              const errorList = document.createElement("ul");
              errorMessageAccount.appendChild(errorList);

              //loop for showing validation errors
              for (const err in result) {
                const error = document.createElement("li");
                error.innerHTML = result[err].join();
                errorList.appendChild(error);
              }

              errorList.classList.add("list");
              errorMessageAccount.style.setProperty("display", "block");
            });
          }
        });
      }
      return false;
    };

    // show first immediately
    $(".account_create")
      .modal({
        onDeny: function () {
          $(".account_create").hide();
        },
        onApprove: function () {
          errorMessageAccount.style.removeProperty("display");
          $("#account").submit();
          return false;
        },
      })
      .modal("show");

    //Parent form validation
    $("#parent").form({
      fields: {
        "parent-name": "empty",
        "parent-category": "empty",
      },
    });

    //Account form validation
    $("#account").form({
      fields: {
        "account-name": "empty",
        "account-country": "empty",
        "account-industry": "empty",
        "account-parent_account": "empty",
        "account-assigned_to": "empty",
      },
    });
  };
});
