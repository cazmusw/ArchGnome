#!/bin/sh

set -e

OS_NAME=$(uname -s)
JB_PRODUCTS="idea clion phpstorm goland pycharm webstorm webide rider datagrip rubymine appcode dataspell gateway jetbrains_client jetbrainsclient studio devecostudio"

BASE_PATH=$(dirname $(
  cd $(dirname "$0")
  pwd
))

JAR_FILE_PATH="${BASE_PATH}/ja-netfilter.jar"

if [ ! -f "${JAR_FILE_PATH}" ]; then
  echo 'ja-netfilter.jar not found'
  exit 1
fi

# GNOME uses environment.d or shell profiles
ENVIRONMENTD_DIR="${HOME}/.config/environment.d"
PROFILE_PATH="${HOME}/.profile"
ZSH_PROFILE_PATH="${HOME}/.zshrc"
BASH_PROFILE_PATH="${HOME}/.bashrc"
ENV_FILE="${ENVIRONMENTD_DIR}/jetbrains.conf"

mkdir -p "${ENVIRONMENTD_DIR}"
touch "${PROFILE_PATH}" "${BASH_PROFILE_PATH}" "${ZSH_PROFILE_PATH}"

MY_VMOPTIONS_SHELL_NAME="jetbrains.vmoptions.sh"
MY_VMOPTIONS_SHELL_FILE="${HOME}/.${MY_VMOPTIONS_SHELL_NAME}"
echo '#!/bin/sh' >"${MY_VMOPTIONS_SHELL_FILE}"

EXEC_LINE='___MY_VMOPTIONS_SHELL_FILE="${HOME}/.jetbrains.vmoptions.sh"; if [ -f "${___MY_VMOPTIONS_SHELL_FILE}" ]; then . "${___MY_VMOPTIONS_SHELL_FILE}"; fi'

# Clean old line from profiles
sed -i '/___MY_VMOPTIONS_SHELL_FILE="${HOME}\/\.jetbrains\.vmoptions\.sh"; if /d' "${PROFILE_PATH}" >/dev/null 2>&1
sed -i '/___MY_VMOPTIONS_SHELL_FILE="${HOME}\/\.jetbrains\.vmoptions\.sh"; if /d' "${BASH_PROFILE_PATH}" >/dev/null 2>&1
sed -i '/___MY_VMOPTIONS_SHELL_FILE="${HOME}\/\.jetbrains\.vmoptions\.sh"; if /d' "${ZSH_PROFILE_PATH}" >/dev/null 2>&1

echo "${EXEC_LINE}" >>"${PROFILE_PATH}"
echo "${EXEC_LINE}" >>"${BASH_PROFILE_PATH}"
echo "${EXEC_LINE}" >>"${ZSH_PROFILE_PATH}"

# Clear previous environment file
> "${ENV_FILE}"

for PRD in $JB_PRODUCTS; do
  VM_FILE_PATH="${BASE_PATH}/vmoptions/${PRD}.vmoptions"
  if [ ! -f "${VM_FILE_PATH}" ]; then
    continue
  fi

  sed -i '/^\-javaagent:.*[\/\\]ja\-netfilter\.jar.*/d' "${VM_FILE_PATH}"
  echo "-javaagent:${JAR_FILE_PATH}=jetbrains" >>"${VM_FILE_PATH}"

  ENV_NAME=$(echo $PRD | tr '[:lower:]' '[:upper:]')"_VM_OPTIONS"
  echo "export ${ENV_NAME}=\"${VM_FILE_PATH}\"" >>"${MY_VMOPTIONS_SHELL_FILE}"
  echo "${ENV_NAME}=${VM_FILE_PATH}" >> "${ENV_FILE}"
done

echo "done. Please reboot or re-login for changes to take effect."
